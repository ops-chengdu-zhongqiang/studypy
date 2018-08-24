# Changelog

## 0.2.7 (2017-06-09)


### New

```
* 增加对haoHR平台的支持. [woodenrobot]

```

### Changes

```
* 升级到0.2.7. [likaiguo]

```

## 0.2.6 (2017-06-08)


### New

```
* Get_url_id()和get_platform()增加对卓聘网的支持. [woodenrobot]

```

### Changes

```
* 升级fabx版本0.1.2. [likaiguo]

* 升级新版本, 针对 work_years 是 string 类型,数据库中是 int 类型处理. [weijinlong]

* Changelog文档生成. [likaiguo]

```

## 0.2.5 (2017-06-07)


### New

```
* 增加对人才啊平台支持. [woodenrobot]

  - get_url_id()支持拉钩网三种简历地址解析
  - PLATFORM_CHOICES增加对e成网和人才啊支持

```

### Fix

```
* Bugfix: 修复ResumeData内部public_status, choices错误. [likaiguo]

```

## 0.2.4 (2017-06-06)


### Changes

```
* 版本升级到0.2.4,添加相关文档. [likaiguo]

* 将WorkExperience的函数和字段进行分离. [likaiguo]

  - 完善相关文档

* BaseAccountCrawInfo()增加server和can_download字段. [woodenrobot]

* Get_platform()增加对miaohr支持. [woodenrobot]

* 优化get_platform()函数，增加账号爬取简历数据库配置. [woodenrobot]

```

### Fix

```
* 修复get_url_id bug. [woodenrobot]

  - 修复get_url_id中获取亿封智联source_id错误的bug

```

### Other

```
* Add: get_url_id()和get_platform()增加对赶集、拉钩的支持. [woodenrobot]

```

## 0.2.3 (2017-05-10)


### Changes

```
* 将WorkExperience的函数和字段进行分离. [likaiguo]

* 将WorkExperience的函数和字段进行分离. [likaiguo]

* BaseAccountCrawInfo()增加server和can_download字段. [woodenrobot]

* Get_platform()增加对miaohr支持. [woodenrobot]

```

## 0.2.2 (2017-05-10)


### New

```
* 添加新的平台支持. [likaiguo]

  - 新增亿封和妙招
  - get_url_id变动支持

```

### Changes

```
* 将WorkExperience的函数和字段进行分离. [likaiguo]

* 优化get_platform()函数，增加账号爬取简历数据库配置. [woodenrobot]

* BaseCollectedResume类增加json_data字段. [woodenrobot]

```

### Fix

```
* 修复get_url_id bug     - 修复get_url_id中获取亿封智联source_id错误的bug. [woodenrobot]

```

## 0.2.0 (2017-04-28)


### New

```
* 添加新的平台支持. [likaiguo]

  - 新增亿封和妙招
  - get_url_id变动支持

```

### Changes

```
* 增加get_url_id()函数对亿封网四种不同类型网址的解析. [woodenrobot]

* Person 表扁平化. [weijinlong]

* 修改ResumeData模型,完善get_url_id. [likaiguo]

  - fix: 对大街网的url解析进行修正
  - chg: 修改共有方法get_url_id位置

```

### Fix

```
* 修复mongo_to_dict dict转类型问题. [likaiguo]

```

## 0.1.8 (2017-03-24)


### New

```
* 新增模型. [likaiguo]

  - Feed 职位
  - RecruitingAccount各个平台招聘账号
  - 图像验证码

```

### Changes

```
* 修改ResumeData模型,完善get_url_id. [likaiguo]

  - fix: 对大街网的url解析进行修正
  - chg: 修改共有方法get_url_id位置

```

## 0.1.4 (2017-01-18)


### New

```
* 新增模型. [likaiguo]

  - Feed 职位
  - RecruitingAccount各个平台招聘账号
  - 图像验证码

```

### Changes

```
* 添加ResumeData字段. [likaiguo]

```

## 0.1.3 (2017-01-09)


### New

```
* 添加新的模型,支持新方法. [likaiguo]

  - 主要是扩展爬虫部分SearchResult,使其支持搜索结果页概要简历
  - 新增get_resume_from_url等方法

```

### Changes

```
* ResumeDataBrief调整. [hexiaosong]

* 增加评测报告模型. [weijinlong]

* ResumeDataBrief添加get_works_segment方法. [hexiaosong]

```

## 0.1.2 (2016-12-30)


### New

```
* 添加新的模型,支持新方法. [likaiguo]

  - 主要是扩展爬虫部分SearchResult,使其支持搜索结果页概要简历
  - 新增get_resume_from_url等方法

* 基础文档. [likaiguo]

  - 完善tutorial文档
  - todo:
    - 定义tox相关配置
    - 完善相关nosettests,coverage,tox,Jenkins工作
    - 加入更多基类

```

## 0.1.1 (2016-12-19)


### New

```
* 基础文档. [likaiguo]

  - 完善tutorial文档
  - todo:
    - 定义tox相关配置
    - 完善相关nosettests,coverage,tox,Jenkins工作
    - 加入更多基类

```

## 0.1.0 (2016-12-19)


### New

```
* 初始化数据库模型. [likaiguo]

```

### Changes

```
* 重新定义依赖,生成相关文档. [likaiguo]

* 项目初始化. [likaiguo]

  - 调整目录结构
  - 忽略不重要文件
  - 初始化文档docs
  - 初始化测试框架
  - 初始化安装包依赖
  - 初始化setup.py

```

### Other

```
* Initial commit. [likaiguo]

```

