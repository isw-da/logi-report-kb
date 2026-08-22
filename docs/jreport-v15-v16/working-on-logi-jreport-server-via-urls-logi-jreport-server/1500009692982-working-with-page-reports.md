---
title: "Working with Page Reports"
id: 1500009692982
section: "Working on Logi JReport Server via URLs Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692982-Working-with-Page-Reports
updated_at: 2021-11-03T06:56:24Z
---

# Working with Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692962-Working-with-Dashboards)

# Working With Page Reports

Besides working on interfaces, most of the Page Report Studio operations such as filter, sort, search, save and so on, can also be accomplished via URL. When using URLs to access Page Report Studio, you should follow the specifications described in this topic.

The URL in Page Report Studio is:

`http://localhost:8888/dhtml?sessionid=XXXXXXX&rptsetid=XXXXXXX&rptname=XXXXXXX&op=...`

* **http**  
  The web service protocol.
* **localhost**  
   The host address.
* **8888**  
  The port.
* **dhtml?sessionid=XXXXXXX&rptsetid=XXXXXXX&rptname=XXXXXXX&**  
  The path.
* **?**  
   URL separator.
* **=**  
  URL separator.
* **&**  
   URL separator.
* **op**  
  The key of operation in Page Report Studio.

There are some methods in the file API.js located in `<install_root>\public_html\javascript\dhtml`. These methods are the tools you can use to generate URLs. The result of each of these functions will be a URL.

| Parameter Description | Key | Value |
| --- | --- | --- |
| Download Report | | |
| Operation code | op | 51 |
| Export report type | ty | 2 for PDF, 3 for PostScript, 4 for RTF, 5 for Text, 6 for Excel, and 7 for XML. |
| Example | `op=51&ty=2` | |
| Note | * The order begins with 2. * A file of HTML type cannot be downloaded. | |
| Prototype | function user\_downloadReport(type) | |
| Exit | | |
| Prototype | function user\_exit (popwin) | |
| Navigate Page | | |
| Operation code | op | 24 |
| Page number | pn | 1...n |
| Example | `op=24&pn=2` | |
| Note | The page number begins with 1 and is less than total page number. | |
| Prototype | function user\_firstPage()  function user\_lastPage()  function user\_nextPage()  function user\_prevPage() | |
| One Step Filter | | |
| Operation code | op | 25 |
| The column name | col | Mapping the name of a column in Logi JReport. |
| Operator of filter condition | operator | eq (equal to), gt (greater than or equal to), geq (greater than), lt (less than), leq (less than or equal to), neq (unequal to) |
| The column value | value |  |
| Logic of filter condition | logic | AND, OR, END |
| Instance name of the column | comp | component instance name | |
| Example | `op=25&col=CusID&operator=eq&value=1&logic=OR&col=CusName&operator=0&value=ZhangKe&logic=2&comp=convert_sectionObject` | |
| Note | The value is case-sensitive. | |
| Prototype | function user\_oneStepfilter(columns, operators, values, logics, instanceName) | |
| One Step Search | | |
| Operation code | op | 128 |
| The column name | column | Mapping the name of a column in Logi JReport. |
| The column value | value | the value to search for |
| Whether or not to search content only | isContent | true/false |
| Whether or not to match case | isMatchCase | true/false |
| The search direction | isUp | true/false |
| Whether or not to match whole word | isWholeWord | true/false |
| Example | `op=128&column=CusID&value=1&isContent=true&isMatchCase=false&isUp=false&isWholeWord=false` | |
| Prototype | function user\_oneStepSearch(value, isContent, colName, isUp, matchcase, isWholeWord) | |
| One Step Sort | | |
| Operation code | op | 12 |
| The column name | col | Mapping the name of a column in Logi JReport. |
| The column sort order | ord | true/false |
| Instance name of the column | comp | component instance name | |
| Example | `op=12&col=CusID&ord=true&col=CusName&ord=false&comp=convert_sectionObject` | |
| Note | The value is case-sensitive. | |
| Prototype | function user\_oneStepSort(columns, sorts, instanceName) | |
| Redo | | |
| Operation code | op | 85 |
| Example | `op=85` | |
| Prototype | function user\_redo() | |
| Refresh | | |
| Operation code | op | 83 |
| Example | `op=83` | |
| Prototype | function user\_refresh() | |
| Reset | | |
| Operation code | op | 76 |
| Example | `op=76` | |
| Prototype | function user\_reset() | |
| Save Report | | |
| Operation code | op | 82 |
| Example | `op=82` | |
| Prototype | function user\_saveRpt() | |
| Search Next | | |
| Operation code | op | 34 |
| Example | `op=34` | |
| Show Export to Dialog | | |
| Prototype | function user\_showSaveResultDialog() | |
| Show Help | | |
| Dialog ID | HELP\_OP | 182 |
| Example | `http://localhost:8888/dhtmljsp/help.jsp?sessionid=XXXXXXX&rptsetid=XXXXXXX&rptname=XXXXXXX&HELP_OP=XXX` | |
| Note | The URL gets the body of a window, you should put it as xxx in `window.open("xxx", ..)` | |
| Prototype | function user\_showHelp(helpId) | |
| Show Panel or Dialog | | |
| Prototype | function user\_showUserPanel()  function user\_showTOC()  function user\_showDHTMLView()  function user\_showToolbox()  function user\_showSortDialog()  function user\_showFilterDialog()  function user\_showNewRptDialog()  function user\_showOpenRptDialog()  function user\_showSaveAsDialog()  function user\_showPageSetupDialog()  function user\_showSaveResultDialog()  function user\_showPageSetupDialog()  function user\_showPrintDialog() | |
| Undo | | |
| Operation code | op | 84 |
| Example | `op=84` | |
| Prototype | function user\_undo() | |
| Zoom | | |
| Operation code | op | 50 |
| Proportion | val | 0~400 |
| Example | `op=50&val=250` | |
| Note | val must be an integer between 0 and 400 | |
| Prototype | function user\_zoom(value) | |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692962-Working-with-Dashboards)
