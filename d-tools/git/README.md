## git找回历史的`commit id`

查看历史操作：
`git reflog`

切换到需要的分支
`git checkout dev`

比较代码，选择需要的保留
`git cherry-pick [commitid]`

## 设置代理

```sh
# 设置代理
git config --global https.proxy http://127.0.0.1:1080

git config --global https.proxy https://127.0.0.1:1080

# 取消代理
git config --global --unset http.proxy

git config --global --unset https.proxy
```