---
title: "Localizing Page Navigation Links in HTML Output"
id: 45190620048013
section: "Applying National Language Support - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190620048013-Localizing-Page-Navigation-Links-in-HTML-Output
updated_at: 2026-04-30T15:15:20Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Localizing Page Navigation Links in HTML Output

Before exporting a report to HTML, you can  localize the names of the page navigation links in the report, such as First, Previous, Next, and Last. This topic describes how you can localize the page navigation link names to display them in another language in HTML output.

- Create the subfolders in <designer_install_root>: <designer_install_root>\resources\report\languages\[language-country]\properties. For example, C:\LogiReport\Designer\resources\report\languages\zh-cn\properties. Designer uses the two-letter codes of the language and country as defined by ISO-639 and ISO-3166 in the folder name.

- Create a report.properties file in the properties folder.

- Open the property file and copy the following content to it. # The following is the report properties file format that can localize the link names in HTML.
4000101=First
4000102=Prev
4000103=Next
4000104=Last
4000105=Back
4000106=Refresh
4000107=@CurrentPageNumber; of @TotalPageNumber;

- Translate the text after "=". For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the language you want. In the HTML output, Report Engine replaces "@CurrentPageNumber"  by the current page number, and "@TotalPageNumber" by the report total page number.    

- Save the property file with UTF-8 encoding.

- Copy the property file to the <jdk_install_root>\bin folder.

- Convert the content in the property file into Unicode using native2ascii.exe in <jdk_install_root>\bin, by running the following command:
    C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties

 When you convert a property file to the same folder as the original one, you need to give the file a new name instead of replacing the original in order to avoid problems.

- Delete report.properties in <designer_install_root>\resources\report\languages\[language-locale]\properties and copy newreport.properties in <jdk_install_root>\bin to it, and then name the property file back to report.properties.

- Start Designer and open a report that contains multiple pages.

- Select the language in which you define the property file from the Language drop-down list in the Home or View ribbon.

- Navigate to File > Export > HTML to export the report to HTML. Make sure you do not select No Hyperlink and No Page Number.

- Open the HTML output. The page navigation links display in the language you specify.
