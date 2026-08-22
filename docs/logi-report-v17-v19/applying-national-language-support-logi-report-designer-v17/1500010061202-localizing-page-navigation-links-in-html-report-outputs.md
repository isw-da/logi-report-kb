---
title: "Localizing Page Navigation Links in HTML Report Outputs"
id: 1500010061202
section: "Applying National Language Support - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs
updated_at: 2021-07-23T19:16:18Z
---

# Localizing Page Navigation Links in HTML Report Outputs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061182-Using-the-Built-in-Functions-for-NLS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099701-Example-of-Creating-an-NLS-Report)

# Localizing Page Navigation Links in HTML Report Outputs

Before exporting a report to HTML, you can localize the names of the page navigation links in the report, such as First, Previous, Next, and Last. This topic describes how you can localize the page navigation link names to display them in your preferred language in the HTML outputs.

1. Create the sub directories in `<designer_install_root>` as follows: `<designer_install_root>\resources\report\languages\[language-locale]\properties`. For example, `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\resources\report\languages\zh-cn\properties`.

   The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The locale argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
2. Create a **report.properties** file in the "properties" directory.
3. Open the property file and copy the following contents to it:

   `# The following is the report properties file format that can localize the link names in HTML.  
   4000101=First  
   4000102=Prev  
   4000103=Next  
   4000104=Last  
   4000105=Back  
   4000106=Refresh  
   4000107=@CurrentPageNumber; of @TotalPageNumber;`
4. Translate the text after "=" to the specified language.

   For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the desired language. In the HTML output, Logi Report replaces "@CurrentPageNumber" by the current page number, and "@TotalPageNumber" by the report total page number.
5. Save the property file with UTF-8 encoding.
6. Copy the property file to the `<jdk_install_root>\bin` directory.
7. Convert the contents in the property file into Unicode using **native2ascii.exe** in `<jdk_install_root>\bin` by running the following command:

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties`

   ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) When you convert a property file to the same directory as the original one, you need to give the file a new name instead of replacing the original in order to avoid problems.
8. Delete report.properties in `<designer_install_root>\resources\report\languages\[language-locale]\properties` and copy **newreport.properties** in `<jdk_install_root>\bin` to it, and then name the property file back to **report.properties**.
9. Start Designer and open a multi-page report, select the language defined for the property file from the **Language** drop-down menu on the **Home** or **View** menu tab.
10. Select **File** > **Export** > **HTML** to export the report to HTML (make sure you do not select **No Hyperlink** and **No Page Number**).
11. Open the HTML output. The page navigation links display in the language you specify.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061182-Using-the-Built-in-Functions-for-NLS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099701-Example-of-Creating-an-NLS-Report)
