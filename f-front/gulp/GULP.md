# gulp简单使用(这里下载3.9，4.0后有较大变化)

将`gulp`安装到本地和项目中。

安装gulp的插件：gulp-cssnano，用于压缩css文件：`npm install gulp-cssnano --save-dev`

```js
//压缩css文件到dist/css目录下，没有则自动创建目录
var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    // .pipe(rename({"suffix":".min"}))  //加上这一句就是重命名,加后缀
    .pipe(gulp.dest("./dist/css/"))
});

```
### 创建项目以及初始化

创建目录结构：`front`
```
front
│   gulpfile.js
│   package.json # init项目时生成
│
└───dist
│   │
│   └───css
│   │   
│   └───js
│   │   
│   └───img
│      
└───src
│   │  
│   └───css
│   │   
│   └───js
│   │   
│   └───img
│      
└───templates
│      
└───node_module # 将包安装到项目中自动生成
```

初始化项目
```powershell
gulp init
```
下载需要的`gulp`插件
```powershell
var cssnano = require("gulp-cssnano"); # 压缩css
var rename = require("gulp-rename"); # 重命名
var gulify = require('gulp-uglify');# 压缩js
var concat = require('gulp-concat');# 不清楚
var cache = require('gulp-cache');# 不清楚，和图片有关
var imagemin = require("gulp-imagemin");# 压缩图片
var bs = require("browser-sync").create();# 异步浏览器
var sass = require("gulp-sass"); #将scss转为css
var util = require("gulp-util"); # 不清楚
var sourcemaps = require("gulp-sourcemaps");# 不清楚
```
根目录创建`gulpfile.js`，并编写任务。

```js
// 1. 引入所有包，这里只引入了一个
var gulp = require("gulp");
//2. 编辑目录路径。方便修改
var path = {
    'html': './templates/**/',//templates下的任意目录下的html
    'css': './src/css/',
    'js': './src/js/',
    'img': './src/img/',
    'css_dist': './dist/css/',
    'js_dist': './dist/js/',
    'img_dist': './dist/img/',
}
//3. 编辑处理html、css、js、img文件的任务,这里给出一个处理css的任务
gulp.task("css",function () {
    gulp.src(path.css + "*.scss")
    .pipe(sass().on("error",sass.logError))//将scss转为css
    .pipe(cssnano())//压缩css
            .pipe(rename({ "suffix": ".min" }))//重命名
        .pipe(gulp.dest(path.css_dist))//存储
        .pipe(bs.stream())//重新写入流中
});
//4. 定义监听文件修改的任务
gulp.task("watch",function () {
    gulp.watch(path.html + ".html",["html"]);
    gulp.watch(path.css + ".html",["css"]);
    gulp.watch(path.js + ".html",["js"]);
    gulp.watch(path.img + ".html",["img"]);
    });

//5. 初始化browser-sync任务，
gulp.task("bs", function () {
    bs.init({
        'server': {
            'baseDir': './'
        }
    })
});

//6. 默认任务，创建服务器，监听修改任务名为default时，可直接使用gulp 不带任务名。
gulp.task("default", ['bs', 'watch']);
```

## [前端](./前端.md)

### 准备工作

引入`jquery3.3.1`到dist/js中。编写`index.js`放入src中。

由于在`gulpfile.js`中使用了监听文件修改的任务。所以，当`index.js`被修改时，会在dist/js中创建index.min.js文件。

在主页面中导入dist中的jquery和index.min.js后就可以编写前端页面了。