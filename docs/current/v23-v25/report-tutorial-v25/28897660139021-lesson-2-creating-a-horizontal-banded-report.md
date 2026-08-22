---
title: "Lesson 2: Creating a Horizontal Banded Report"
id: 28897660139021
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897660139021-Lesson-2-Creating-a-Horizontal-Banded-Report
updated_at: 2026-02-26T02:10:41Z
source_host: docs-report.zendesk.com
---
# Lesson 2: Creating a Horizontal Banded Report

Your new reporting assignment is to create a summary of each Jinfonet Gourmet Java employee. The report also needs to communicate the ranking of the employee's salary, that is, whether it is on the upper or lower end, or somewhere in between, relative to all employees.

The following prototype of the report has been given to you:

Follow these tasks to create the report:

- Task 1: Create the Initial Report

- Task 2: Adjust the Report Layout  and Add the Photo DBField 

- Task 3: Rank the Employees

- Task 4: Fine Tune the Report Layout

## 
Task 1: Create the Initial Report

Again, the report has repeated rows of information, but this time they are repeated left to right instead of top down. Report offers the horizontal banded layout to support this format. 

To create the initial report with a horizontal banded object, follow these steps:

- In  Designer, navigate to File > New > Page Report. Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see Task 1, Steps 3 and 4 of Lesson 1.    

- In the Select Component for Page Report dialog box, select Horizontal Banded, then select OK.
    

- In the Data screen of the Horizontal Banded Wizard dialog box, select <New Query...> in the Queries node of Data Source 1,  type EmployeeInformation in the Enter Query Name dialog box and select OK.

- In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the Tables node, then select the table Account Managers and select Add to add it to the query. Select OK to close the dialog box.

- In the Query Editor dialog box, select * in the Account Managers table to add all the columns in it to the query and then select OK to create the query.

- Select Next in the Horizontal Banded Wizard dialog box to go to the next screen.

- In the Display screen, drag the following DBFields from the Resources box to the right box one by one: Name, Employee Position, Notes, HireDate, Birthday, and Home Phone, then edit the display names of HireDate and Birthday to Hire Date and Birth Date. Select Next.
    

- In the Group screen, select Account Manager ID and select Add to add it as the group-by field.

- Select Style on the screen navigation bar to switch to the screen and select Simple as the report style.

- Select Finish to create the report.    Designer identifies the panels in the banded object on the top by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a group header panel (GH), a detail panel (DT), a group footer panel (GF), a banded page footer panel (BPF), and a banded footer panel (BF).

## 
Task 2: Adjust the Report Layout and Add the Photo DBField 

In this task, we want to adjust the layout of the report first to improve the appearance of the report. Then, we need to add the Photo field to the report which enables users of the report  to identify the employee. 

- Widen the DT panel, then resize the Employee Position and Notes DBFields horizontally so that the data does not get truncated.
    

- Select the Name, Employee Position, and Notes labels in the BPH panel, then select Delete on the keyboard to remove them from the report.
    

- Adjust the space between fields in the DT panel, move the Hire Date, Birth Date, and Home Phone name labels from the BPH panel to the DT panel and place them above their fields. 

- Hide the BH, BPH, GF, BPF, and BF panels that do not hold any data by right-clicking the panel and selecting Hide from the shortcut menu.

- Resize the GH panel, navigate to Insert > Label to add a label before the group-by field in the panel, double-click the label to edit its text as "Employee ID:", then resize the group-by field and the label and adjust their position as follows:
    

- From the Data panel, drag the Photo DBField  to the GH panel.

- Remove the name label of the Photo DBField by right-clicking it and selecting Delete from the shortcut menu, then resize the field as follows:
    

- Navigate to Insert > Drawing Object > Line to insert a Line object below the first field in the DT panel, and insert a box object in the same way to enclose all the objects in the reports.
    

## 
Task 3: Rank the Employees

As required at the beginning of the report design, the manager wants to rank the employees by their salaries, so we need to add a rank object to the report.

- Select the DT panel of the report and navigate to Insert > Rank.

- In the Rank Expert dialog box, select Salary from the Rank Resources box.

- Select Browse, choose Rank5.gif in the JinfonetGourmetJava folder and select Open to select it as the default image for all value ranges.

- In the Value Range box,  type 40000 in the Minimum column and 49999 in Maximum, then select in the Image column and select <Browse...> to choose Rank3.gif as the image of this range.

- Select Add twice to add two ranges and define them as follows:
    

- Select Insert to insert the rank to the DT panel, below the Home Phone field.

- Move the name label Salary of the rank from the bottom of GH panel and place it above the rank, then edit its text to Salary Ranking and resize the label to full display the text.
    

## 
Task 4: Fine Tune the Report Layout

- Select the Employee ID label and the group-by field in the GH panel, then select  10 from Font Size drop-down list  in the Format ribbon.

- Select the Salary Ranking label and the rank in the DT panel, then navigate to Format > Left  to align them the same with other objects in the DT panel.

- Select the first field in the DT panel (the Name DBField), change its properties in the Report Inspector as follows, then resize it to make sure the names can display completely.
    
- Font Size: 12

- Bold: true

- Foreground: 0xcc0000

- Right-click the Photo DBField in the GH panel and select Display Type from the shortcut menu.

- In the Display Type dialog box, select Image in the Display As box, choose GIF or JPG from the Decode Type drop-down list, then select OK.
    

- In the Report Inspector, select the Line node in the report structure tree and change its Line Color property to Lightgray and Line Thickness to 0.02.
    

- Select the Box node and change its Border Color property to Lightgray too.

Next, we want to add a title to the report to the page header panel of the report. 

- Select Page Header in the View ribbon to display the page header.

- In the Report Inspector, select the Page Header Panel node and change its Height property to 0.6.

- From the Components panel, drag the Label icon  to the page header panel to add a label in it.

- Resize the label, double-click it to modify its text as Employee Information List, then in the Report Inspector, change its Font Size to 14, and Foreground to 0xcc0000.
    After editing, the report looks somewhat as follows in design view:

- On the report tab bar, right-click the report tab and select Rename to rename it to EmployeeDetails.
    

- Navigate to File > Save to save the report as EmployeeInformation.cls.

- Select the View tab to preview the report. Designer displays the report similar to this:
    

 If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the JinfonetGourmetJava.cat catalog file in <install_root>\Demo\Reports\TutorialReports.
