---
title: "Why Web Reports and When to Choose Them"
id: 1500009778881
section: "Web Report Studio Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778881-Why-Web-Reports-and-When-to-Choose-Them
updated_at: 2021-07-24T00:47:28Z
---

# Why Web Reports and When to Choose Them

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750002-Components-Supported-in-Web-Reports)

# Why Web Reports and When to Choose Them

Web Report Studio displays web reports (also web layout reports) that aim at easier and faster report creation and design, faster report execution, easier customization, and better presentation style using the newest Web technology. This topic describes major benefits of using web reports.

Web reports also support agile development techniques such as continuous integration by allowing report templates to be updated by both Web Report Studio and Logi Report Designer.

* **Fewer functions**  
   Web reports (.wls) support a subset of functions of Logi Report page reports (.cls). The basic and essential functions not only guarantee a good report presentation, but also make the report design experience easier for a new user of Logi Report.
* **Single report solution**  
   Only one report in a web report speeds up the report running process as compared to a multiple-report page report.
* **Tabular style layout**  
   The creation of a page report using the Standard Report Wizard can only create one data component (table, crosstab, chart, or banded object) using the wizard. The Web Report Wizard provides predefined tabular-look layouts for determining the absolute positions of the components in a report. You can place a data component in each cell so as to achieve a holistic layout with multiple components from the very beginning.
* **Predefined report templates**  
   Web reports allow you to choose a starting template so you can predefine the template to include standard features such as company logo, company name, privacy notices or any standard items and styles you want your users to start with.
* **Fast report rendering**  
   At runtime, Web Report Studio provides much higher performance when viewed from a browser compared to viewing a page report using Page Report Studio. Using Page Report Studio, all the user action requests must be sent to Logi Report Server which renders the new page on the server and updates the browser view. Using Web Report Studio, many of the actions which require only a change in rendering the view are done locally on the client in the browser. Logi Report Engine is structured so that as much of the processing as possible is completed on the client side allowing much higher scalability for Logi Report Server allowing the server to handle more simultaneous users.
* **Creation and modification in both Logi Report Server and Designer**  
  Web reports created using the Web Report Wizard can be downloaded from Logi Report Server and edited in Logi Report Designer and web reports can be created in Logi Report Designer and published to server just like .cls reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750002-Components-Supported-in-Web-Reports)
