---
title: "Making HTML and PDF Report Results and Server Console Accessible"
id: 1500009718642
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718642-Making-HTML-and-PDF-Report-Results-and-Server-Console-Accessible
updated_at: 2021-07-25T07:20:20Z
---

# Making HTML and PDF Report Results and Server Console Accessible

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718302-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744021-References-Logi-Report-Server-v17)

# Making HTML and PDF Report Results and Server Console Accessible

You can export reports to accessible HTML and PDF results and enable the accessible version of Logi Report Server for people who experience disabilities or have special needs, so they can access the reports using assistive tools. This topic describes how you can add accessibility to HTML report results, export reports to accessible PDF files, and enable the accessible version of Logi Report Server. It also briefly introduces the functionality of the accessible version of Logi Report Server.

Select the following links to view the topics:

* [Exporting Reports to Accessible PDF Files](#PDF)
* [Making HTML Format Report Result Accessible](#HTML)
* [Visiting the Accessible Version of Logi Report Server](#Server)

## Exporting Reports to Accessible PDF Files

You can export reports to accessible PDF files, by enabling the Accessible PDF option which is available on all PDF export UIs in Logi Report, so that users of screen readers and those who have low vision can have their tagged PDF files read out aloud in appropriate language in the Adobe Acrobat software. The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) <http://www.w3.org/TR/WCAG/>and the PDF/UA (ISO 14289-1) standard <http://www.iso.org/standard/64599.html>.

## Making HTML Format Report Result Accessible

Logi Report supports accessibility related HTML attributes and a built-in accessible Logi Report Server console for displaying the report result in HTML format. The implementation standard is based on HTML specification 4.01 <http://www.w3.org/TR/WCAG10-HTML-TECHS/> and information on Section 508 Standards [http://www.access-board.gov](http://www.access-board.gov/).

When designing a report in Logi Report Designer, you can add the accessibility related HTML attributes to the report elements in order to make the HTML format result more readable and accessible. You can find those attributes in the Accessibility category of the Report Inspector.

**To add accessibility to a report in the HTML format result:**

1. Predefine necessary accessibility attributes when designing the report in Logi Report Designer.
2. Enable Section 508 compliant output when exporting the report to HTML format.

   In the HTML export UI, select **Section 508 Compliant Output**. If you only want to convert table/crosstab components into HTML data table in the HTML format report result, select **Use HTML Data Table**.

   The above two options are available on all HTML export UIs in Logi Report.

## Visiting the Accessible Version of Logi Report Server

You can visit the accessible version of Logi Report Server with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version, Logi Report Server displays reports in the HTML format with accessibility attributes and displays table/crosstab components as HTML data tables.

You can use the option - Use Accessible Version- to set the accessible version of Logi Report Server as the default portal UI. The default port for accessible version is 8888 which is also the default port for the Logi Report Server console in normal version. That is to say, the **Use Accessible Version** option controls switching between normal version and accessible version of Logi Report Server UI when logging onto port 8888. By default, this option is unselected and you are directed to the server console in normal version.

The server administrator can activate the accessible version for all users or for an individual user:

* **For all users:**
  1. In the Logi Report Server console, point to **Administration** on the system toolbar, select **Server Profile** > **Customize Server Preferences** from the drop-down menu.
  2. Select the **Advanced** tab.
  3. Select the **Use Accessible Version** option.
  4. Select **OK** to apply the change.
* **For an individual user:**
  1. In the server console, point to **Administration** on the system toolbar, select **Security** > **User** from the drop-down menu.
  2. Locate the wanted user ID, then select the  **Preference** link for the user.
  3. In the Preference dialog box, go to the **Advanced** tab.
  4. Select **Use Accessible Version**.
  5. Select **OK** to save the change.

You can also enable the accessible version for yourself in the following way:

1. In the server console, select **My Profile** > **Customize Server Preferences** on the system toolbar
2. Select the **Advanced** tab.
3. Select the **Use Accessible Version** option.
4. Select **OK** to save the change.

After you have been enabled the access to Accessible Version, you will be directed to the accessible version after logging in next time. You can navigate through the server resource to view the target report, with the help of reader agent.

See the main options that are available on the accessible version UI:

* **Directory Path**Displays the current directory where you have come to follow the server resource tree.
* **Up to Higher Level Directory**Goes to the parent level folder.
* **Up to Top Level Directory**Goes to the default portal page.
* **Leave Accessible Version**  
   Redirects to the normal version of the server console with full functionalities. Once you leave the accessible version, there is no way to return unless you re-log in. However, it is not recommended for the disabled to leave the accessible version unless having others' help.
* **Select User Directory**You can choose to open either the My Reports folder or the Public Reports folder.
* **Catalog**  
   Lists the catalogs used in the current directory.
* **Report List**  
   Lists the folders and reports in the current directory. You can select the hyperlinks in the Name column to open them.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718302-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744021-References-Logi-Report-Server-v17)
