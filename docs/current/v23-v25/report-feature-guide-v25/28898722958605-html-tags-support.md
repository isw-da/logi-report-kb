---
title: "HTML Tags Support"
id: 28898722958605
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898722958605-HTML-Tags-Support
updated_at: 2025-05-30T03:01:44Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
HTML Tags Support

HTML tags serve as the fundamental building blocks of web pages, providing code elements that instruct browsers on how to display content. In the context of Report, HTML tags play a crucial role in maintaining consistent layouts across various static result formats such as PDF, HTML, and Excel. You have the flexibility to store data with HTML tags in databases, XML files, web services, and more. Regardless of the data source, Report engine adeptly handles HTML-tagged data based on your configurations.

Report offers two approaches for HTML Tags support: Ignore HTML Tags and Parse and Render HTML Tags.

## Ignore HTML Tags

You can opt to have browsers interpret HTML tag content by setting the "Ignore HTML Tag" property to TRUE on a report element.

- 
Pros: Easy setup.
            

- 
Cons: Different browsers may render HTML tags differently, leading to varied results. Additionally, other formats like PDF, Excel, and Word are not supported.
            

## Parse and Render HTML Tags

Report parses and renders HTML tags directly in reports. You can load HTML tag data from databases, XML, or services into text-based elements, including fields and labels within tables, banded objects, or crosstabs. Alternatively, you can directly paste HTML tag content into labels in a report. When reports with these HTML tags are run, the results are consistently displayed across various formats such as Page Report Studio, PDF, HTML, Excel, and RTF. As of Report v24.1, most common HTML tags are supported.

See the following examples:

Displaying an apple logo in a PDF using SVG tags

<svg xmlns="SVG namespace " viewBox="0 0 90 100" width="90" height="100">   <path d="M62,0c2,10-9,24-20,24c-3-14,9-22,20-24M5,36c5-8,13-12,21-12c7,0,12,4,19,4c6,0,10-4,19-4c6,0,14,3,19,10c-16,4-15,35,3,39c-7,17-18,27-24,27c-7,0-8-5-17-5c-9,0-11,5-17,5c-7-1-13-7-17-13c-9-10-15-40-6-51" fill="#AAA"/> </svg>
Here is the PDF result exported from Report:

Using image tags with URL

Code: 

<img src="https://www.w3school.com.cn/i/eg_tulip.jpg" alt="by url" width="400" height="266"/>
Result:

Nested ordered and unordered lists for indented numbering and bullets

Code:

<ol> <li> Drink <ol> <li>Coffee</li> <li>Tea</li> <li>Milk</li> </ol> </li> <li> Fruit <ol> <li>Apple</li> <li>Orange</li> <li>Banana</li> </ol> </li> </ol>
Result:

Code:

<ul> <li> Drink <ul> <li>Coffee</li> <li>Tea</li> <li>Milk</li> </ul> </li> <li> Fruit <ul> <li>Apple</li> <li>Orange</li> <li>Banana</li> </ul> </li> </ul>
Result:

Table tags for creating structured tables

<table> <tr> <th>Header1</th> <th>Header2</th> </tr> <tr> <td>Bread</td> <td>Shop</td> </tr> <tr> <td>Coffee</td> <td>Apple</td> </tr> <tr> <td>Tea</td> <td>Orange</td> </tr> <tr> <td>Milk</td> <td>Banana</td> </tr> </table>
Result:

Applying formatting tags such as <i> for italics

<i>bike</i>
Result: bike

Report also supports base64-encoded SVG for SVG tags.

Previous Topic  Next Topic
