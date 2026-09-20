#!/usr/bin/env python3
"""Build the beginner guide from the eight independently editable content chapters.

Requires reportlab. Output defaults to output/pdf/CISSP-Beginner-Study-Guide.pdf.
Wide source tables become labeled records so no columns require tiny print.
"""
from pathlib import Path
import argparse, html, re
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.platypus.tableofcontents import TableOfContents
ROOT=Path(__file__).resolve().parents[1]
NAVY=colors.HexColor('#17324D');TEAL=colors.HexColor('#236B70');INK=colors.HexColor('#263238');PALE=colors.HexColor('#EEF4F5');GRAY=colors.HexColor('#596773')
NAMES=['Security and Risk Management','Asset Security','Security Architecture and Engineering','Communication and Network Security','Identity and Access Management','Security Assessment and Testing','Security Operations','Software Development Security']
WEIGHTS=[16,10,13,13,13,12,13,10]
LINK=re.compile(r'\[([^\]]+)\]\(([^()]*(?:\([^()]*\)[^()]*)*)\)')

def clean(s):
 for a,b in [('—',' - '),('–','-'),('‑','-'),('−','-'),('\u00a0',' '),('\u200b',''),('‘',"'"),('’',"'"),('“','"'),('”','"'),('…','...'),('→',' -> '),('↔',' <-> '),('≤',' <= '),('≥',' >= '),('≠',' != '),('✅','Yes'),('❌','No')]:s=s.replace(a,b)
 return s

def slug(s):
 s=LINK.sub(r'\1',s).replace('**','').replace('`','').lower()
 return re.sub(r'\s+','-',re.sub(r'[^\w\s-]','',s))

def inline(s,domain=0):
 s=clean(s);held=[]
 def hold(mark):held.append(mark);return f'ZZLINKTOKEN{len(held)-1}ZZ'
 def link(m):
  label,url=m.groups();url=url.strip()
  if url.startswith('#'):
   target=url[1:]
   if not target.startswith(('objective-','subtopic-','domain-')):target=f'd{domain}-{target}'
   url='#'+target
  elif re.match(r'CISSP-Domain-(\d+)-Content.md',url):
   match=re.match(r'CISSP-Domain-(\d+)-Content.md(?:#(.*))?',url);url='#'+(match[2] or 'domain-'+match[1])
  elif url.startswith('../CISSP-'):
   url='https://github.com/jefferywmoore/CISSP-Study-Resources/blob/main/'+url[3:]
  elif not re.match(r'^(https?://|mailto:|#)',url):
   return hold(html.escape(label))
  label=html.escape(label).replace('**','').replace('`','')
  return hold(f'<link href="{html.escape(url,quote=True)}" color="#236B70">{label}</link>')
 s=re.sub(r'<(https?://[^>]+)>',r'[\1](\1)',s)
 s=LINK.sub(link,s)
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',s)
 for i,v in enumerate(held):s=s.replace(f'ZZLINKTOKEN{i}ZZ',v)
 return s

def styles():
 fonts=Path('/System/Library/Fonts/Supplemental')
 if (fonts/'Arial.ttf').exists():
  for name,file in [('Guide','Arial.ttf'),('GuideBold','Arial Bold.ttf'),('GuideItalic','Arial Italic.ttf'),('GuideBoldItalic','Arial Bold Italic.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
  pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='GuideItalic',boldItalic='GuideBoldItalic')
  regular,bold='Guide','GuideBold'
 else:regular,bold='Helvetica','Helvetica-Bold'
 st=getSampleStyleSheet()
 for name,size,leading,color,before,after in [('Body',10.3,14.4,INK,0,7),('Domain',25,30,NAVY,0,15),('H2',15,19,NAVY,17,8),('H3',12,16,TEAL,12,6),('H4',10.5,14,TEAL,9,4),('Small',8.5,11.5,GRAY,0,5),('Index',8.2,11,INK,0,2),('Cover',34,39,NAVY,0,18)]:
  st.add(ParagraphStyle(name=name,fontName=bold if name in ['Domain','H2','H3','H4','Cover'] else regular,fontSize=size,leading=leading,textColor=color,spaceBefore=before,spaceAfter=after,keepWithNext=name in ['Domain','H2','H3','H4'],splitLongWords=True,allowWidows=0,allowOrphans=0))
 for name,level in [('TOC0',0),('TOC1',1)]:st.add(ParagraphStyle(name=name,fontName=bold if not level else regular,fontSize=11 if not level else 9.4,leading=15,spaceBefore=7 if not level else 0,leftIndent=14*level,rightIndent=24,textColor=NAVY))
 return st

class Book(BaseDocTemplate):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs);self.current_domain=0
  self.addPageTemplates(PageTemplate(id='book',frames=[Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.draw_page))
 def beforeDocument(self):self.current_domain=0
 def afterFlowable(self,f):
  if hasattr(f,'domain'):self.current_domain=f.domain
  if hasattr(f,'toc'):
   level,title,key=f.toc;self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level,closed=True);self.notify('TOCEntry',(level,title,self.page,key))
 def draw_page(self,c,doc):
  c.saveState();w,h=letter
  if doc.page>1:
   c.setStrokeColor(colors.HexColor('#CDDADD'));c.line(self.leftMargin,h-35,w-self.rightMargin,h-35)
   c.setFont('Helvetica',8);c.setFillColor(GRAY);c.drawString(self.leftMargin,h-25,'CISSP | BEGINNER STUDY GUIDE')
   c.drawRightString(w-self.rightMargin,h-25,'2026 study edition')
   c.line(self.leftMargin,35,w-self.rightMargin,35);c.drawString(self.leftMargin,23,'Independent study resource | 2024 objectives with AI guidance')
   c.drawRightString(w-self.rightMargin,23,str(doc.page))
  c.restoreState()

def build(output):
 st=styles();doc=Book(str(output),pagesize=letter,leftMargin=52,rightMargin=52,topMargin=51,bottomMargin=50,title='CISSP Beginner Study Guide',author='CISSP Study Resources contributors',subject='Eight domains, objective-based explanations and AI applications')
 story=[Spacer(1,56),Paragraph('CISSP<br/>Beginner Study Guide',st['Cover']),Paragraph('Eight domains. Connected explanations.<br/>Practical decisions and AI applications.',st['H2']),Spacer(1,17),HRFlowable(width='100%',thickness=3,color=TEAL),Spacer(1,21),Paragraph('September 2026 study edition',st['H3']),Paragraph('Aligned to the CISSP exam outline effective April 15, 2024, with AI guidance integrated into existing objectives.',st['Body']),Spacer(1,17),Paragraph('How to read this book',st['H3']),Paragraph('Begin with each objective\'s explanation, explore the detailed concepts, then answer the application question before reading the reasoning. Harbor Services provides a shared example across the domains. Use the contents and chapter term indexes to revisit unfamiliar concepts.',st['Body']),Paragraph('This independent guide adapts the repository\'s study notes and adds teaching explanations. It is not an ISC2 publication or an official scoring rubric. Historical technologies are included for comparison. Sources appear beside relevant material and at the end of each chapter.',st['Small']),Paragraph('Based on CISSP Study Resources by Jeffery W. Moore and repository contributors, distributed under the repository\'s Apache License 2.0. This edition contains editorial adaptations and additional examples.',st['Small']),PageBreak(),Paragraph('The eight domains',st['H2'])]
 rows=[[Paragraph('Domain',st['H4']),Paragraph('Focus',st['H4']),Paragraph('Weight',st['H4'])]]
 for n,name in enumerate(NAMES,1):rows.append([Paragraph(str(n),st['Body']),Paragraph(name,st['Body']),Paragraph(str(WEIGHTS[n-1])+'%',st['Body'])])
 t=Table(rows,colWidths=[48,doc.width-105,57],repeatRows=1);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#CDDADD')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story+=[t,Spacer(1,18),Paragraph('A shared example',st['H3']),Paragraph('Harbor Services is a small organization introducing an online customer portal and considering an AI support assistant. Follow its decisions about risk, information, architecture, communication, identity, assurance, operations, and development. The scenarios are teaching examples; several solutions may be defensible when their assumptions and evidence differ.',st['Body']),PageBreak(),Paragraph('Contents',st['H2'])]
 toc=TableOfContents();toc.levelStyles=[st['TOC0'],st['TOC1']];story+=[toc,PageBreak()]
 anchors=set()
 def p(text,style='Body',domain=0,ids=None):
  prefix=''
  for a in ids or []:
   if a not in anchors:prefix+=f'<a name="{a}"/>';anchors.add(a)
  return Paragraph(prefix+inline(text,domain),st[style])
 for n in range(1,9):
  file=ROOT/'content'/f'CISSP-Domain-{n}-Content.md';lines=file.read_text().splitlines();i=0;pending=[];index=False;nav=False
  while i<len(lines):
   line=lines[i].strip()
   if not line:i+=1;continue
   a=re.fullmatch(r'<a id="([^"]+)"></a>',line)
   if a:pending.append(a[1]);i+=1;continue
   h=re.match(r'^(#{1,4}) (.+)',line)
   if h:
    level=len(h[1]);title=h[2]
    nav=title=='Chapter navigation';index=title=='Term index'
    if nav:i+=1;continue
    ids=pending+[f'd{n}-'+slug(title)];pending=[]
    flow=p(title,['','Domain','H2','H3','H4'][level],n,ids)
    if level==1:flow.domain=n;flow.toc=(0,clean(title),f'book-domain-{n}')
    elif level==2 and re.match(r'^\d+\.\d+ ',title):flow.toc=(1,clean(title),'book-'+re.match(r'^(\d+\.\d+)',title)[1].replace('.','-'))
    story.append(flow);i+=1;continue
   if nav:i+=1;continue
   if line.startswith('|'):
    rows=[]
    while i<len(lines) and lines[i].strip().startswith('|'):
     cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
     if not all(re.fullmatch(r'[:\- ]+',x) for x in cells):rows.append(cells)
     i+=1
    width=max(map(len,rows));rows=[r+['']*(width-len(r)) for r in rows]
    if width>4:
     headers=rows[0]
     for row in rows[1:]:
      story.append(p(row[0],'H4',n))
      for label,value in zip(headers[1:],row[1:]):
       if value:story.append(p(f'**{label.replace("**", "")}:** {value}','Body',n))
    else:
     table=Table([[p(c,'Small',n) for c in r] for r in rows],colWidths=[doc.width/width]*width,repeatRows=1,hAlign='LEFT')
     table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#CDDADD')),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story += [table,Spacer(1,9)]
    continue
   if line.startswith('- '):
    items=[]
    while i<len(lines) and (not lines[i].strip() or lines[i].startswith('- ')):
     if lines[i].startswith('- '):items.append(lines[i][2:])
     i+=1
    if index:
     cells=[p(x,'Index',n) for x in items];rows=[cells[j:j+3]+['']*(3-len(cells[j:j+3])) for j in range(0,len(cells),3)]
     table=Table(rows,colWidths=[doc.width/3]*3);table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]));story.append(table)
    else:
     for x in items:story.append(p('• '+x,'Small',n))
    continue
   para=[line];i+=1
   while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#{1,4} |<a |\||- )',lines[i]):para.append(lines[i].strip());i+=1
   story.append(p(' '.join(para),'Body',n,pending));pending=[]
  if n<8:story.append(PageBreak())
 output.parent.mkdir(parents=True,exist_ok=True);doc.multiBuild(story)
 print(output)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=ROOT/'output/pdf/CISSP-Beginner-Study-Guide.pdf');args=parser.parse_args();build(args.output)
