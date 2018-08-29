## 部署

### 创建 Python 虚拟环境

    $ pyenv virtualenv 3.6.5 pytesseract-server
    $ pyenv activate pytesseract-server

### 安装项目依赖包

    $ make pip

### 启动服务

    $ make run-dev

## 依赖的 OCR 项目

- [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://github.com/madmaze/pytesseract)

## Web 前端

Web 前端界面直接用了 [otiai10/ocrserver](https://github.com/otiai10/ocrserver)

## heroku 部署

    $ heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
    $ heroku config:set TESSDATA_PREFIX=/app/.apt/usr/share/tesseract-ocr/tessdata

    $ cat Aptfile
    tesseract-ocr
    libtesseract-dev
