---
title: "Why Web Reports and When to Choose Them"
id: 1500009675401
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675401-Why-Web-Reports-and-When-to-Choose-Them
updated_at: 2021-07-24T20:53:33Z
---

# Why Web Reports and When to Choose Them

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports)

# Why Web Reports and When to Choose Them

Web Report Studio displays web reports (which are also called web layout reports) that are aimed at easier and faster report creation and design, faster report execution, easier customization, and better presentation style using the newest Web technology. Web reports also support agile development techniques such as continuous integration by allowing report templates to be updated by both Web Report Studio and Logi JReport Designer.

* **Fewer functions**  
   Web reports (.wls) support a subset of functions of Logi JReport page reports (.cls). The basic and essential functions not only guarantee a good report presentation, but also make the report design experience easier for a new user of Logi JReport.
* **Single report solution**  
   Only one report in a web report speeds up the report running process as compared to a multiple-report page report.
* **Tabular style layout**  
   The creation of a page report using the Standard Report Wizard can only create one data component (table, crosstab, chart, or banded object) using the wizard. The Web Report Wizard provides a tabular style layout in which you can place a table, crosstab or chart in each tabular cell so as to achieve a holistic layout with multiple components from the very beginning.
* **Predefined report templates**   
   Web reports allow you to choose a starting template so you can predefine the template to include standard features such as company logo, company name, privacy notices or any standard items and styles you want your users to start with.
* **Fast report rendering**  
   At runtime, Web Report Studio provides much higher performance when viewed from a browser compared to viewing a page report using Page Report Studio. Using Page Report Studio, all of the user action requests must be sent to Logi JReport Server which renders the new page on the server and updates the browser view. Using Web Report Studio, many of the actions which require only a change in rendering the view are done locally on the client in the browser. By using Web Report Studio, Logi JReport Engine is structured so that as much of the processing as possible is completed on the client side allowing much higher scalability for Logi JReport Server allowing the server to handle more simultaneous users.
* **Creation and modification in both Logi JReport Server and Designer**  
  Web reports created using the Web Report Wizard can be downloaded from Logi JReport Server and edited in Logi JReport Designer and web reports can be created in Logi JReport Designer and published to server just like .cls reports.

  Also, Logi JReport Designer can be used to create web reports which can be run in Web Report Studio on the server and saved as a template to use in Web Report Studio. Logi JReport Designer cannot directly create the template but can create the report and then using Web Report Studio, save the report as a template (.wsld).
* **Standard banded objects not supported**  
  Page reports support standard banded objects which are not supported by web reports.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports)
