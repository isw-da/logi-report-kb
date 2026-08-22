---
title: "Exporting to Fax"
id: 1500009610962
section: "Delivering Your Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610962-Exporting-to-Fax
updated_at: 2021-07-24T16:03:59Z
---

# Exporting to Fax

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611022-Exporting-to-PostScript) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources)

# Exporting to Fax

Logi Report Designer provides the feature of exporting the report result to fax either via a fax machine or a fax server. If you require this feature to be enabled, you will first need to configure your running environment.

This topic includes the following sections:

* [Configuring the Fax Settings](#Config)
* [Exporting a Report to Fax](#Export)

## Configuring the Fax Settings

**To configure the settings for exporting report result to fax via a fax machine:**

1. Configure the running environment first. Download Java Communications API (Version 2.0) for [Win32](http://www.jinfonet.com/download/third_party_tool/JavaCommAPIV2_Win32.zip) or [Solaris](http://www.jinfonet.com/download/third_party_tool/JavaCommAPIV2_Solaris.zip), and place the following files in the specified locations:
   * For Windows:  

     | File Name | Location |
     | --- | --- |
     | comm.jar | `<designer_install_root>\lib` |
     | javax.comm.properties | `<Java_install_root>\jre\lib` |
     | Win32Com.dll | `<Java_install_root>\jre\bin` |
   * For Solaris:   

     | File Name | Location |
     | --- | --- |
     | comm.jar | `<designer_install_root>/lib` |
     | javax.comm.properties | `<Java_install_root>/jre/lib` |
     | libSolarisSerialParallel.so | `LD_LIBRARY_PATH` |
2. Select **File** > **Options**.
3. In the Options dialog, select the **Export to** category.
4. Select the **Fax** tab. The Fax Machine radio button is selected by default.

   ![Fax Machine Settings](https://devnet.logianalytics.com/hc/article_attachments/4404904227351/frmt_expt_fax1.gif)
5. From the Dialing drop-down list, select the dialing mode for the fax modem: Tone or Pulse.
6. From the Modem Class drop-down list, select the class of the modem: Class 1, Class 2 or Class 2.0. Most modems only support Class 1, so if you select Class 2 or Class 2.0, you should make sure that your modem can support it.
7. In the Initialization String text box, type in the string to initialize the modem. The string should be obtained from your modem manual.
8. From the Flow Control drop-down list, select the flow control mode between DTE (Data Terminal Equipment) and DCE (Data Circuit-terminating Equipment). Specifying flow control can help the compressing data function of the modem work better.
   * **RtsCts**  
      Flow control of the hardware (recommended).
   * **Xon/Xoff**  
      Flow control of the software.
   * **None**  
      No flow control specified.
9. From the Flow Command drop-down list, select the flow control command according to the modem being used. If not contained in the drop-down list, you can leave this empty and specify the command as part of the initial string. The command should be obtained from your modem manual.
10. In the Port text box, type
    the port number. The port should be obtained from your modem manual.
11. Specify the maximum amount of time that the fax should wait for a response from the destination before timing out.
12. When the line is busy, the report result cannot be faxed, so you can specify the maximum number of times the modem re-tries faxing the report result in the Retries text box.
13. Select **OK** to accept the settings.

**To configure the settings for exporting report result to fax via a fax server:**

1. Select **File** > **Options**.
2. In the Options dialog, select the **Export to** category.
3. Select the **Fax** tab, then select the **Fax Server** radion button.

   ![Fax Server Settings](https://devnet.logianalytics.com/hc/article_attachments/4404911671703/frmt_expt_fax2.gif)
4. In the Fax Gateway Connector text box, type the name of the implemented class.

   By default, the fax server Logi Report uses is based on Hylafax Server, however if you want to export your report result via Hylafax Server, you need to download the gnu-hylafax packages according to your requirements from <http://sourceforge.net/projects/gnu-hylafax/>, for example, gnu-hylafax-util-0.0.9.2.jar, gnu-inet-ftp-0.0.9.2.jar, and gnu-hylafax-0.0.9.2.jar, and then add them to the class path of the file setenv.bat in `<designer_install_root>\bin`.
5. In the Server IP text box, type the IP address or domain name of the fax server.
6. In the Server Port text box, type the port number of the fax server.
7. In the Login ID text box, type the username for the class communicating with fax server.
8. In the Password text box, type the password for the class communicating with fax server.
9. In the Fax Sender text box, specify the user's name that is shown in the fax server manager.
10. In the Special Parameters text box, specify the parameters for the fax server.
11. Specify the maximum amount of time that the fax should wait for a response from the destination before timing out. For Hylafax Server the value should not be larger than 59 seconds. It is a limitation of Hylafax Server.
12. In the Retries text box, type the number of times the modem retries faxing the report result.
13. Select **OK** to accept the settings.

## Exporting Reports to Fax

After you have configured the fax settings in the Options dialog, you can now export your reports to fax as follows:

1. Open the report you want to export.
2. Select **File** > **Export** > **To Fax**. The [Export to Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009608102-Export-to-Fax-Dialog) dialog appears.

   ![Export to Fax dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904227863/expt2fax.gif)
3. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404911669015/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904224919/btn_mvdwn3.gif) to change the order of the report tabs.
4. Specify the quality of the fax: Best, Normal, or Fast.
5. Choose whether to send a cover sheet with the fax.
6. Specify what you want to display on the cover sheet if you select to include it.
   * **Fax Number**  
      Specifies the fax number of the recipient.
   * **Phone Number**  
      Specifies the phone number of the sender.
   * **To**  
      Specifies information of the recipient.
   * **From**  
      Specifies information of the sender.
   * **Company**  
      Specifies information of the company.
   * **Date**  
      Specifies the day on which the fax is sent.
   * **RE**  
      Specifies the subject of the fax.
   * **Comments**  
      Specifies some comments to the fax.
   * **Urgent**  
      Specifies whether the fax is urgent.

* **For Review**  
   Specifies whether or not only review is required for the fax.
* **Please Comment**Specifies whether or not comments are required for the fax.
* **Please Reply**  
   Specifies whether or not a reply is required for the fax.

7. Select **Run Linked Report** if you want to generate the reports that is linked with the report (not including the detail reports) in the fax result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. Select **OK** to start exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611022-Exporting-to-PostScript) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources)
