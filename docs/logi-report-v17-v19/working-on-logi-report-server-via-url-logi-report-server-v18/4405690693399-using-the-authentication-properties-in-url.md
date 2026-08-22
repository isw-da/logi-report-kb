---
title: "Using the Authentication Properties in URL"
id: 4405690693399
section: "Working on Logi Report Server via URL Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690693399-Using-the-Authentication-Properties-in-URL
updated_at: 2022-01-27T07:59:55Z
---

# Using the Authentication Properties in URL

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684052759-Creating-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684055959-Working-with-Server-via-URL)

# Using the Authentication Properties in URL

Logi Report Server requires that you be authenticated before you can access any web pages. This topic describes how you can use the authentication properties in URL.

When using URL to work on Logi Report Server, if you have not previously been authenticated, you can include the authentication properties in the URL to pass in signing in credentials. This is a proprietary signing in protocol Server develops to make it easy to identify a user by passing along the signing in request in the URL along with the operation request.

You can use the following authentication properties to pass in the signing in credentials.

* **jrs.authorization**  
   Tag of the HTTP query field jrs.authorization.  
   Description: Load the requested page with the specified credential information. You should not use this method outside of a firewall, although it looks like it is encrypted it is not secure.  
   Format of the value of the HTTP query field: Base64-encoded (userID:password). For more information, see <http://en.wikipedia.org/wiki/Base64>.  
   In the following examples, the user ID and password are both set as admin, so the value of the HTTP query field is Base64-encoded("admin:admin")="YWRtaW46YWRtaW4=".
  + `http://localhost:8888/jrserver?jrs.cmd=jrs.get_subnodes&jrs.authorization=YWRtaW46YWRtaW4%3D.`
  + `http://localhost:8888/jreport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Dashboard - Coffee Sales.dsh","ver":-1}]}&jrs.authorization=YWRtaW46YWRtaW4%3D`

* **jrs.auth\_uid and jrs.auth\_pwd**  
   Tags of HTTP query field: jrs.auth\_uid and jrs.auth\_pwd.  
   Description: Load the requested page with the specified credential information.  
   Format of the value of the HTTP query field: jrs.auth\_uid=USER\_ID, jrs.auth\_pwd=PASSWORD.  
   Examples:
  + This URL requests the JSP page viewVersion.jsp with credentials passed in to sign in the user "scott" with the password "tiger":  
    `http://localhost:8888/jinfonet/viewVersion.jsp?jrs.cmd=jrs.view_ver_def&jrs.rst_version=1&jrs.ver_suff=.pdf&jrs.report=/Payroll Report.cls&jrs.auth_uid=scott&jrs.auth_pwd=tiger`
  + This URL runs the dashboard with credentials passed in to sign in the user "scott" with the password "tiger":  
    `http://localhost:8888/jreport/dashboard/app/entry/run.jsp?jrd_resext={"active":0,"reslst":[{"name":"/SampleReports/Dashboard - Coffee Sales.dsh","ver":-1}]}&jrs.auth_uid=scott&jrs.auth_pwd=tiger`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)JRServlet does not perform authentication check when an HTTP request has no jrs.cmd in the HTTP query in the root path of JRServlet, and also does not accept the jrs.authorization and jrs.auth\_uid & jrs.auth\_pwd for the request.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684052759-Creating-Reports-via-URL)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684055959-Working-with-Server-via-URL)
