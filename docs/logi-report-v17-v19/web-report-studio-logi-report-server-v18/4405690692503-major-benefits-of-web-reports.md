---
title: "Major Benefits of Web Reports"
id: 4405690692503
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690692503-Major-Benefits-of-Web-Reports
updated_at: 2022-01-27T07:59:55Z
---

# Major Benefits of Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684033815-Components-Supported-in-Web-Reports)

# Major Benefits of Web Reports

Web Report Studio displays web reports (also web layout reports) that aim at easier and faster report creation and design, faster report execution, easier customization, and better presentation style using the newest Web technology. This topic describes major benefits of using web reports.

Web reports also support agile development techniques such as continuous integration, by allowing you to update report templates by both Web Report Studio and Logi Report Designer.

* **Fewer functions**  
   Web reports that use .wls as the file suffix, support a subset of functions of Logi Report page reports that use .cls as the file suffix. The basic and essential functions not only guarantee a good report presentation, but also make the report design experience easier for a new user of Logi Report.
* **Single report solution**  
   Only one report in a web report speeds up the report running process as compared to a multiple-report page report.
* **Tabular style layout**  
   The creation of a page report using the Standard Report Wizard can only create one data component (table, crosstab, chart, or banded object) at a time. The Web Report Wizard provides predefined tabular-look layouts for determining the absolute positions of the components in a report. You can place a data component in each cell to achieve a holistic layout with multiple components from the very beginning.
* **Predefined report page templates**  
   Web reports allow you to choose a starting page template so you can predefine the template to include standard features such as company logo, company name, privacy notices, or any standard items and styles you want your users to start with.
* **Fast report rendering**  
   At runtime, Web Report Studio provides much higher performance when viewed from a browser compared to viewing a page report using Page Report Studio. Page Report Studio must send all the user action requests to Logi Report Server which renders the new page on the server and updates the browser view. Web Report Studio does many of the actions locally on the client in the browser, because they require only a change in rendering the view. Logi Report Engine enables as much of the processing as possible to complete on the client side, allowing much higher scalability for Logi Report Server to handle more simultaneous users.
* **Creation and modification in both Logi Report Server and Designer**  
  After you create web reports using the Web Report Wizard, you can download them from Logi Report Server and edit them in Logi Report Designer. You can also create web reports in Logi Report Designer and then publish them to Server just like page reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684033815-Components-Supported-in-Web-Reports)
