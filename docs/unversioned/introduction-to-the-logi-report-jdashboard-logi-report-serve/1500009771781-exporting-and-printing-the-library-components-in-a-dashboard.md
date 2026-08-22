---
title: "Exporting and Printing the Library Components in a Dashboard"
id: 1500009771781
section: "Introduction to the Logi Report JDashboard Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771781-Exporting-and-Printing-the-Library-Components-in-a-Dashboard
updated_at: 2021-07-24T00:49:25Z
---

# Exporting and Printing the Library Components in a Dashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743882-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743922-Running-and-Editing-Reports-in-JDashboard)

# Exporting and Printing the Library Components in a Dashboard

You can export and print library components visible in the page panel, for example, library components that you created using Logi Report Designer and then inserted into dashboards via the Resources panel. This topic describes how you can export and print library components in a dashboard, using either the system layout or customized layout.

When you export or print the library components in a dashboard, you can choose whether to use the system layout or customize the layout by yourself. In the system layout, Logi Report will calculate the positions of the library components in the dashboard following certain rule. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to export or print all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. You can save the customized layout for all users who can access the dashboard.

This topic contains the following sections:

* [Exporting the Library Components in a Dashboard Using the System Layout](#ExportSystem)
* [Exporting the Library Components in a Dashboard Using a Customized Layout](#ExportCustom)
* [Exporting a Single Library Component Using a Convenient Way](#ExportSingle)
* [Printing the Library Components in a Dashboard Using the System Layout](#PrintSystem)
* [Printing the Library Components in a Dashboard Using a Customized Layout](#PrintCustom)

## Exporting the Library Components in a Dashboard Using the System Layout

1. Take either of the following ways:
   * Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif) on the toolbar.
   * Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) on the toolbar and then select **Export** from the option list.

   JDashboard displays the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009773361-Export-Dialog-Box-Properties#Dashboard) dialog box.
2. JDashboard selects the **System Layout** item as the layout by default.

   ![Export dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/4404880561815/expt_dshbd_sys.gif)

   JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
3. In the **Resources** box, select the library components you want to export. By default, JDashboard lists and selects all exportable library components.
4. The order of the library components in the **Resources** box determines the order in which JDashboard export them. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) to adjust the exporting order.
5. Select the **Show Component Title** option if you want to show the library component titles in the exported result.
6. You can select the page navigation buttons on the toolbar of the preview panel to browse the pages.
7. Select the **Page Setup** icon ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/4404885524503/btn_dshbrd_pgstup.gif) on the toolbar. JDashboard displays the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties#Export) dialog box.

   ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885525143/pgstup_gnrl.gif)
8. Set the page properties for the exported result file, such as page size and margins. You can either define the page properties generally for all export formats or customize the page properties for each export format as you want.
9. Select the **Export** icon ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif). JDashboard displays the **Export** dialog box.
10. From the **Export File Format** drop-down list, select the format to which you want to export the library components. For a format other than XML, JDashboard will export all the selected library components into one single file. For XML, JDashboard will export each library component to a separate XML file. When the exported result contains more than one file, JDashboard will zip all the files.
11. In the **File Name** text box, specify the name of the exported result file, which could be either a single file or a zipped package name.
12. Select **Run Linked Report** if you need to include linked report in the exported result file.
13. Select **OK** to start exporting.

## Exporting the Library Components in a Dashboard Using a Customized Layout

1. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif) on the toolbar. JDashboard displays the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009773361-Export-Dialog-Box-Properties#Dashboard) dialog box.
2. Select **Customize Layout** from the **Layout** drop-down list. You can also select an existing customized layout to modify it.

   ![Export dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/4404880452759/expt_dshbd.gif)
3. Select the **Show Component Title** option if you want to show the library component titles in the exported result.
4. Select the **Page Setup** icon ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/4404885524503/btn_dshbrd_pgstup.gif) on the toolbar. JDashboard displays the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties#Export) dialog box.

   ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885525143/pgstup_gnrl.gif)
5. Set the page properties for the exported result file, such as page size and margins.
6. In the **Design** tab, customize the layout of the library components by making use of the following operations.
   JDashboard arranges the library components using a tabular with each cell holding one component.
   * Split or merge cells using the toolbar icons: **Horizontal Split****![Horizontal Split button](https://devnet.logianalytics.com/hc/article_attachments/4404880440087/btn_dshbrd_splth.gif)**, **Merge****![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404885522967/btn_dshbrd_merge.gif)**, and **Vertical Split****![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/4404885523735/btn_dshbrd_spltv.gif)**.
   * Drag a library component from the **Resources** box into a blank cell in the **Design** tab. A cell can hold only one library component.
   * Delete a library component from a tabular cell using the shortcut menu option **Remove**.
   * For a table or crosstab, JDashboard will only export its current view of data as displayed in the dashboard by default. If you want to export its full data, right-click on the table or crosstab and select **Filter** from the drop-down list. JDashboard displays the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009773381-Filter-Dialog-Box-Properties) dialog box. Switch from **Current View** to **All** and then select **OK**.

     ![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880451735/fltr.gif)
7. Select the **View** tab to preview the layout. You can browse the pages and zoom in/out by selecting the corresponding toolbar buttons.
8. If you are satisfied with the layout and would like to save it for future use, select the **Save** icon ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif) or the **Save As** icon**![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif)** on the toolbar. JDashboard displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009745682-Save-As-Dialog-Box-Properties) dialog box. Provide a name for the layout and select **OK**. JDashboard displays the customized layouts you saved in the **Layout** drop-down list to all users who can access the dashboard. For each of them, you can edit its name or delete it using the two icons - **Rename**![Rename icon](https://devnet.logianalytics.com/hc/article_attachments/4404885605655/btn_dshbrd_rename.gif) and **Delete**![Delete icon](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif) - appearing on the right when the mouse hovers over the layout item in the drop-down list.

   ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404880439703/dshbrd_expt_layout.gif)
9. Select the **Export** icon ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif). JDashboard displays the Export dialog box.
10. [Do the last setting and start exporting.](#Export)

## Exporting a Single Library Component Using a Convenient Way

If you just want to export a single library component, you can use a more convenient method.

1. Select the **Options** icon ![Options Icon](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009771801-General-Operations-in-JDashboard#TitleBar) and then select **Export** from the drop-down menu. JDashboard displays the Export dialog box.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885532951/expt_lc.gif)
2. Choose the format to which you want to export the library component.
3. Select **OK**.

However, using this method, if the library component is linked with other reports, you cannot control whether to generate the linked reports while exporting. JDashboard will not include the linked reports in the exported result.

## Printing the Library Components in a Dashboard Using the System Layout

1. Take either of the following ways:
   * Select the ****Print**** button **![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif)** on the toolbar.
   * Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880435735/btn_dshbrd_optn.gif) on the toolbar and then select **Print** from the option list.

   JDashboard displays the [Print](https://devnet.logianalytics.com/hc/en-us/articles/1500009745562-Print-Dialog-Box-Properties) dialog box.
2. JDashboard selects **System Layout** as the Layout type by default.

   ![Print dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/4404880562455/prnt_sys.gif)

   JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
3. In the **Resources** box, select the library components you want to print. By default, JDashboard lists and selects all printable library components.
4. The order of the library components in the Resources box determines the order in which JDashboard will print them. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) to adjust the printing order.
5. Select the **Show Component Title** option if you want to show the library component titles in the printed result.
6. From the **Printer** drop-down list, select the printer to use to print the library component result. JDashboard lists the printers the web browser can access here. If you want to download the result to a PDF or HTML file and then use your local printer to print the file, select **Save as PDF** or **Save as HTML**.
7. If you select a printer, you can select the **Properties** link to specify the printing properties in the [Printer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009745582-Printer-Properties) dialog box.
8. Define the number of copies you want to print accordingly.
9. Specify the page orientation and paper type for the printed result file. You can select the **More Settings**  link to set more page properties such as paper size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009773581-Page-Setup-Dialog-Box-Properties#Print) dialog box.
10. Select the page navigation buttons on the toolbar of the preview panel to browse the pages.
11. Select the **Print** icon ![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif) on the toolbar to start printing. If you have selected **Save as PDF** or **Save as HTML** in the **Printer** drop-down list, JDashboard will open the result file of the library components in an associated program with which you can print the result to a printer.

## Printing the Library Components in a Dashboard Using a Customized Layout

1. Select the ****Print**** button **![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif)** on the toolbar. JDashboard displays the [Print](https://devnet.logianalytics.com/hc/en-us/articles/1500009745562-Print-Dialog-Box-Properties) dialog box.
2. Select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![Print dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/4404880439191/prnt.gif)
3. Do the same as described in steps 5 to 10 of the above system layout procedure.
4. In the **Design** tab, customize the layout of the library components, then preview it in the **View** tab. For more information, see [Exporting the Library Components in a Dashboard Using a Customized Layout](#ExportCustom).
5. Select the **Print** icon ![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif) on the toolbar to start printing. If you have selected **Save as PDF** or **Save as HTML** in the **Printer** drop-down list, JDashboard will open the result file of the library components in an associated program with which you can print the result to a printer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743882-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743922-Running-and-Editing-Reports-in-JDashboard)
