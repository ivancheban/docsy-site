---
title: "MadCap build failed error"
linkTitle: "MadCap build failed error"
weight: 2
description: >
  Use this instruction to resolve the build error in MadCap Flare.
---

{{% pageinfo %}}
Our goal is to resolve the error 10086 that occurs when you build the MadCap project.
{{% /pageinfo %}}

In MadCap Flare, the 10086 **The process cannot access the file because it is being used by another process** error will prevent you from building your PDF target.

![img](/docs/img/build-error.png)

Such error in my case arises when your MadCap project is bound to Git. You need to commit and push all your changes before building the target.

Another workaround is:

1. Open Windows Task Manager.

2. Select the **AdobeCollabSync.exe** process.

3. Select **End task**.

    ![img](/docs/img/end-task.png)

One more workaround is to use Foxit Reader instead of Adobe Acrobat Reader.