---
id: ${header['function']}
title: ${header['function']}
sidebar_label: ${header['function']}  
---
## -*- coding: utf-8 -*-

%if header['function']:
```python
def ${header['function']}${header['signature']}:
```
%elif header['class']:
${h1} ${header['class']}
```python
class ${header['class']}${header['signature']}:
```
%endif 

%for section in sections:
    %if section['header']:
${h2} ${section['header']}
    %else:
---
    %endif
    %if section['args']:
        %for arg in section['args']:
        %if arg['field']:
* **${arg['field']}** ${arg['signature']} : ${arg['description']}
        %else:
* ${arg['description']}
        %endif
        %endfor
    %endif
${section['text']}
%endfor
