---
title: "Localizing Page Navigation Links in HTML Output"
id: 5735525819287
section: "Applying National Language Support - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525819287-Localizing-Page-Navigation-Links-in-HTML-Output
updated_at: 2022-11-02T08:07:48Z
---

# Localizing Page Navigation Links in HTML Output

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525805335-Using-the-Built-in-Functions-for-NLS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568299159-Example-of-Creating-an-NLS-Report)

# Localizing Page Navigation Links in HTML Output

Before exporting a report to HTML, you can localize the names of the page navigation links in the report, such as First, Previous, Next, and Last. This topic describes how you can localize the page navigation link names to display them in another language in HTML output.

1. Create the subfolders in `<designer_install_root>`: `<designer_install_root>\resources\report\languages\[language-country]\properties`. For example, `C:\LogiReport\Designer\resources\report\languages\zh-cn\properties`. Designer uses the two-letter codes of the language and country as defined by ISO-639 and ISO-3166 in the folder name.
2. Create a **report.properties** file in the **properties** folder.
3. Open the property file and copy the following content to it.

   `# The following is the report properties file format that can localize the link names in HTML.  
   4000101=First  
   4000102=Prev  
   4000103=Next  
   4000104=Last  
   4000105=Back  
   4000106=Refresh  
   4000107=@CurrentPageNumber; of @TotalPageNumber;`
4. Translate the text after "=". For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the language you want. In the HTML output, Logi Report Engine replaces "@CurrentPageNumber" by the current page number, and "@TotalPageNumber" by the report total page number.
5. Save the property file with UTF-8 encoding.
6. Copy the property file to the `<jdk_install_root>\bin` folder.
7. Convert the content in the property file into Unicode using **native2ascii.exe** in `<jdk_install_root>\bin`, by running the following command:

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you convert a property file to the same folder as the original one, you need to give the file a new name instead of replacing the original in order to avoid problems.
8. Delete report.properties in `<designer_install_root>\resources\report\languages\[language-locale]\properties` and copy **newreport.properties** in `<jdk_install_root>\bin` to it, and then name the property file back to **report.properties**.
9. Start Designer and open a report that contains multiple pages.
10. Select the language in which you define the property file from the **Language** drop-down list in the **Home** or **View** ribbon.
11. Navigate to **File** > **Export** > **HTML** to export the report to HTML. Make sure you do not select **No Hyperlink** and **No Page Number**.
12. Open the HTML output. The page navigation links display in the language you specify.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525805335-Using-the-Built-in-Functions-for-NLS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568299159-Example-of-Creating-an-NLS-Report)
