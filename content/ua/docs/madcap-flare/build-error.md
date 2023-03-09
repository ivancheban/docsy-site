---
title: "Помилка білда MadCap"
linkTitle: "Помилка білда MadCap"
weight: 2
description: >
  Використовуйте цю інструкцію, щоб усунути помилку під час компіляції (білда) проекта MadCap Flare.
---

{{% pageinfo %}}
Наша мета — усунути помилку 10086, що виникає під час білда проекта MadCap.
{{% /pageinfo %}}

У MadCap Flare може виникати промилка 10086 **The process cannot access the file because it is being used by another process** під час компіляції проекта в форматі PDF.

![img](/docs/img/build-error.png)

У моєму випадку така помилка виникає, коли проект MadCap прив’язаний до Git. Потрібно передати всі зміни в гіт, перед тим як запустити білд проекта.

Ще один варіант вирішення:

1. Відкрийте диспетчер завдань Windows Task Manager.

2. Виберіть процес **AdobeCollabSync.exe**.

3. Виберіть **Завершити процес**.

    ![img](/docs/img/end-task.png)

Ще один варіант — використовувати Foxit Reader замість Adobe Acrobat Reader.