---
title: "Track 6: Integrating Reports and Dashboards"
id: 1500009561922
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009561922-Track-6-Integrating-Reports-and-Dashboards
updated_at: 2021-07-24T05:56:27Z
---

# Track 6: Integrating Reports and Dashboards

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security)

# Track 6: Integrating Reports and Dashboards

Logi JReport reports and dashboards can be integrated into user applications by using URL or JSP (only available to page reports). You can then work on the integrated reports and dashboards as you do in Logi JReport Server.

In this track, we will integrate some sample reports and dashboards in the /Public Reports/SampleReports folder into an application portal. The application portal allows users to easily request the integrated reports they need while accessing the applications they use. For this track, the application portal is built using frames. The links to the reports and dashboards are added in the application menu and appear on the same page that is the entry point to the application. However in most corporate settings there would be an application portal which would be used to launch the application and common reports. The techniques and code required to call the reports are identical whether it is a portal or a simple menu so the sample code can be utilized in either situation.

The following tasks are covered in the track:

* [Task 1: View the Source for the Application Menu](#Task1)
* [Task 2: View the Application Menu](#Task2)

## Task 1: View the Source for the Application Menu

This track includes HTML which creates a menu on the left frame and displays the requested content in the right side frame.

1. Create a folder jag in the directory `<install_root>\public_html`.
2. Copy the contents in `<install_root>\help\samples\JSPSamples\JinfonetGourmetJavaDemo` to `<install_root>\public_html\jag`.
3. Open index.htm in the jag directory in your favorite editor. This HTML file simply creates two frames, namely leftFrame which displays left.htm and rightFrameSet which by default has introduction.htm in `<install_root>\public_html\jag\application` displayed.
4. Open left.htm in your editor. You will see it is a table with the menu items we want to present to the user.

## Task 2: View the Application Menu

1. Start Logi JReport Server and open a web browser to <http://localhost:8888/jag/index.htm>. The page is something like this:

   ![Application Portal](https://devnet.logianalytics.com/hc/article_attachments/4404894047767/jsp.gif)
2. Select the links in the left frame to view the introduction and integrated reports and dashboards. The following details the sample each link is associated with and the JSP and HTML files that the samples call:
   * **Reporting Introduction**  
      Calls introduction.htm in `<install_root>\public_html\jag\application` to display the introduction of the application. You can also open the introduction by <http://localhost:8888/jag/application/introduction.htm>.
   * **Run Web Report**  
      Calls runWebreport.jsp in `<install_root>\public_html\jag\webreport` to run the specified web report via Web Report Studio in the application. You can also open the sample by <http://localhost:8888/jag/webreport/runWebreport.jsp>.
   * **Run Web Report with Parameter**  
      Calls runWebreportwithparameter.jsp in `<install_root>\public_html\jag\webreport` to run the specified web report with the designated parameter value via Web Report Studio in the application. You can also open the sample by <http://localhost:8888/jag/webreport/runWebreportwithparameter.jsp>.
   * **Export Web Report** Calls exportWebreport.html in `<install_root>\public_html\jag\webreport` to show the sample in which two buttons are provided to open the specified web report and then export it to the desired result format via Web Report Studio. You can also open the sample by <http://localhost:8888/jag/webreport/exportWebreport.html>.
   * **New Dashboard**  
      Calls newDashboard.jsp in `<install_root>\public_html\jag\dashboard` to create a new dashboard via JDashboard in the application. You can also open the sample by <http://localhost:8888/jag/dashboard/newDashboard.jsp>.
   * **View Dashboard**  
      Calls viewDashboard.jsp in `<install_root>\public_html\jag\dashboard` to open two specified dashboards in the application via the view mode of JDashboard. You can also open the sample by <http://localhost:8888/jag/dashboard/viewDashboard.jsp>.
   * **Edit Dashboard**  
      Calls editDashboard.jsp in `<install_root>\public_html\jag\dashboard` to open the specified dashboard in the application via the edit mode of JDashboard. You can also open the sample by [http://localhost:8888/jag/dashboard/editDashboard.jsp](http://localhost:8888/jag/dashboard/viewDashboard.jsp).
   * **New Visual Analysis**  
      Calls newVA.jsp in `<install_root>\public_html\jag\va` to start a new visual analysis session via Visual Analysis in the application. You can also open the sample by <http://localhost:8888/jag/va/newVA.jsp>.
   * **Run Visual Analysis**  
      Calls runVA.jsp in `<install_root>\public_html\jag\va` to open the specified analysis template via Visual Analysis in the application. You can also open the sample by <http://localhost:8888/jag/va/runVA.jsp>.
   * **Run Page Report**  
      Calls runReport.jsp in `<install_root>\public_html\jag` to run the specified page report via Page Report Studio in the application. You can also open the sample by <http://localhost:8888/jag/runReport.jsp>.
   * **Run Page Report with Parameters**  
      Calls runWithParameter.html in `<install_root>\public_html\jag` to request the parameter values used by the specified page report and then runWithParameter.jsp in the same folder to run the page report via Page Report Studio in the application. You can also open the sample by [http://localhost:8888/jag/runWithParameter.html](http://192.168.128.99:8888/jag/runWithParameter.html).
   * **Export Page Report**  
      Calls exportReport.html in `<install_root>\public_html\jag` to to show the sample in which two buttons are provided to open the specified page report and then export it to the desired result format via Page Report Studio. You can also open the sample by <http://localhost:8888/jag/exportReport.html>.
   * **Schedule Page Report**  
      Calls scheduleRequestJS.html, scheduleRequest.html and scheduleReport.jsp in `<install_root>\public_html\jag` to submit a schedule task in the application, which publishes the specified page report to disk in the PDF format. You can also open the sample by <http://localhost:8888/jag/scheduleRequestJS.html>.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security)
