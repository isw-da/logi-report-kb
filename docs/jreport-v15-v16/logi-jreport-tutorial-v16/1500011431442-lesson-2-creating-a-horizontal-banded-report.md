---
title: "Lesson 2: Creating a Horizontal Banded Report"
id: 1500011431442
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431442-Lesson-2-Creating-a-Horizontal-Banded-Report
updated_at: 2021-07-24T10:39:41Z
---

# Lesson 2: Creating a Horizontal Banded Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431422-Lesson-3-Creating-a-Mailing-Label-Report)

# Lesson 2: Creating a Horizontal Banded Report

In this lesson, we will create a horizontal banded report, rank the employees, and fine tune the report layout.

Your new reporting assignment is to create a summary of each Jinfonet Gourmet Java employee. The report will also need to communicate the ranking of the employee's salary, that is, whether it is on the upper or lower end, or somewhere in between, relative to all employees. The following prototype of the report has been given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404901092503/rpt_lsn2_model.gif)

Follow the tasks below to finish creating the report:

* [Task 1: Create the Initial Report](#Task1)
* [Task 2: Adjust the Report Layout and Add the Photo DBField](#Task2)
* [Task 3: Rank the Employees](#Task3)
* [Task 4: Fine Tune the Report Layout](#Task4)

## Task 1: Create the Initial Report

Again the report has repeated rows of information, but this time they are repeated left to right instead of top down. A horizontal banded report is offered to support this format.

To create the initial report with a horizontal banded object, follow these steps:

1. In Logi JReport Designer select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, select **Horizontal Banded**, then select **OK**.

   Be sure that JinfonetGourmetJava.cat is specified as the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the Data screen of the Horizontal Banded Wizard, select **<New Query...>** in the Queries node of Data Source 1, input **EmployeeInformation** in the Enter Query Name dialog and select **OK**.
4. In the Add Tables/Views/Queries dialog, expand the JDBC connection node and then the **Tables** node, then select the table **Account Managers**  and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif) to add it to the query. select **OK** to close the dialog.
5. In the Query Editor, select **\*** in the Account Managers table to add all the columns in it to the query and then select **OK** at the bottom of the editor to create the query.
6. Select **Next** in the Horizontal Banded Wizard to go to the Display screen.
7. From the Resources box, select the following DBFields in the Account Managers table and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif) to add them to the right-hand box one by one: **Name**, **Employee** **Position**, **Notes**, **HireDate**, **Birthday** and **Home Phone**, edit the display names HireDate and Birthday to **Hire Date** and **Birth Date**, then select **Next**.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404909097367/rpt_lsn2_dsply.gif)
8. In the Group screen, select **Account Manager ID** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901075351/btn_addarw.gif) to add it as the group-by field.
9. Select **Style** to switch to the screen and select **Simple** as the report style. select **Finish** to create the report and the report appears as follows:

   ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/4404901092759/rpt_lsn2_intlrpt.gif)

   The panels in the banded object are identified on the top by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a group header panel (GH), a detail panel (DT), a group footer panel (GF), a banded page footer panel (BPF) and a banded footer panel (BF).

## Task 2: Adjust the Report Layout and Add the Photo DBField

To improve the appearance of the report, we will do some adjustments to the report's layout. In addition, we will add a Photo field to the report which allows the report to be used to identify the employee.

1. Widen the DT panel, then resize the **Employee Position** and **Notes** DBFields horizontally so that the data won't get truncated.

   ![Resize DBFields](https://devnet.logianalytics.com/hc/article_attachments/4404901093015/rpt_lsn2_wdn.gif)
2. Select the **Name**, **Employee Position** and **Notes** labels in the BPH panel by holding the Ctrl key on the keyboard and press the **Delete** button on the keyboard to remove them from the report.

   ![Delete Labels](https://devnet.logianalytics.com/hc/article_attachments/4404909097623/rpt_lsn2_dltlbl.gif)
3. Adjust the space between fields in the DT panel, move the **Hire Date**, **Birth Date**, and **Home Phone** name labels from the BPH panel to the DT panel and place them above their fields as follows:

   ![Move Labels](https://devnet.logianalytics.com/hc/article_attachments/4404909097879/rpt_lsn2_spc.gif)
4. Hide the BH, BPH, GF, BPF and BF panels that don't hold any data by right-clicking the panel and select **Hide** from the shortcut menu.
5. Resize the GH panel, select **Insert** > **Label** to add a label before the group field in the panel, edit its text as "**Employee ID:**", resize the group field and the label, and adjust the position like the following:

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/4404909098135/rpt_lsn2_id.gif)
6. From the Data panel, drag the **Photo** DBField in the Account Managers table to the GH panel.
7. Remove the name label of the Photo DBField by right-clicking it and selecting **Delete** from the shortcut menu, then resize the field as follows:

   ![Add Photo](https://devnet.logianalytics.com/hc/article_attachments/4404901093271/rpt_lsn2_photo.gif)
8. Select **Insert** > **Drawing Object** > **Line** to insert a line object below the first field in the DT panel, and insert a box object in the same way to enclose all the objects in the reports.

   ![Insert Drawing Objects](https://devnet.logianalytics.com/hc/article_attachments/4404909098391/rpt_lsn2_box.gif)

## Task 3: Rank the Employees

As required at the beginning of the report design, the manager wants to rank the employees by their salaries, so we will add a rank object to the report.

1. Select the DT panel of the report and select **Insert** > **Rank** to display the Rank Expert dialog.
2. In the Rank Expert dialog, first select **Salary** from the Rank Resources box.
3. Select the **Browse** button, choose **Rank5.gif** in the JinfonetGourmetJava folder and select **Open** to select it as the default image for all value ranges.
4. In the Value Range box, input **40000** in the Minimum cell, **49999** in the Maximum cell, then select in the **Image** cell and select **<Browse...>** to choose **Rank3.gif** as the image of this range.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901073303/btn_add.gif) twice to add two ranges and define them as follows:

   ![Define Ranks](https://devnet.logianalytics.com/hc/article_attachments/4404901093527/rpt_lsn2_addrnk.gif)
6. Select the **Insert** button to insert the rank to the DT panel, below the Home Phone field.
7. Move the name label Salary of the rank from the bottom of GH panel and place it above the rank, then edit its text to **Salary Ranking** and resize the label to full display the text.

   ![Insert Ranks](https://devnet.logianalytics.com/hc/article_attachments/4404909098647/rpt_lsn2_rank.gif)

## Task 4: Fine Tune the Report Layout

1. Select the **Employee ID** label and the group-by field in the GH panel by holding the Ctrl key on the keyboard, then select **10** from the Format > Font Size drop-down list ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404909097111/btn_fontsz.gif).
2. Hold the Ctrl key on the keyboard and select the **Salary Ranking** label and the rank in the DT panel, then select **Format** > **Left**![Left Align button](https://devnet.logianalytics.com/hc/article_attachments/4404909098903/btn_alignleft.gif) so as to make them aligned the same with other objects in the DT panel.
3. Select the first field in the DT panel (the Name DBField), change its properties in the Report Inspector as follows, then resize it to make sure the names can be fully displayed.
   * Font Size: 12
   * Bold: true
   * Foreground: 0xcc0000
4. Right-click the **Photo** DBField in the GH panel and select **Display Type** from the shortcut menu.
5. In the Display Type dialog, select **Image** in the Display As box, choose **GIF or JPG** from the Decode Type drop-down list, then select **OK**.

   ![Display Field as Image](https://devnet.logianalytics.com/hc/article_attachments/4404901093783/rpt_lsn2_img.gif)
6. In the Report Inspector, select the **Line** node in the report structure tree and change its Line Color property to **Lightgray**, Line Thickness to **0.02**.

   ![Edit Line Properties](https://devnet.logianalytics.com/hc/article_attachments/4404909099159/rpt_lsn2_lnprpty.gif)
7. Select the **Box** node and change its Border Color property to **Lightgray** too.

Next, we will add a title to the report to the page header panel of the report.

1. Select **View** > **Page Header** to display the page header.
2. In the Report Inspector, select the **Page Header Panel** node and change its Height property to **0.6**.
3. Drag ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404901080471/btn_label.gif) from the Basic group in the Components panel and drop it in the page header panel.
4. Resize the label, double-click it to modify its text as **Employee Information List**, then in the Report Inspector, change its Font Size to **14**, and Foreground to **0xcc0000**.

   After editing, the report looks somewhat like below in design view:

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/4404901094039/rpt_lsn2_dsgn.gif)
5. On the report tab bar, right-click the report tab and select **Rename** to rename it to **EmployeeDetails**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404901076631/renmrpttb.gif)
6. Select **File** > **Save** to save the report as **EmployeeInformation.cls**.
7. Select the **View** tab to preview the report. The report appears similar to the below one:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404901094295/rpt_lsn2_prvw.gif)

   **Note:** If the report does not look correct, you can compare it to the final version of the report provided by Logi JReport. To do so, you will need to save and close this catalog and then open the JinfonetGourmetJava.cat catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011431462-Lesson-1-Creating-a-Standard-Banded-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431422-Lesson-3-Creating-a-Mailing-Label-Report)
