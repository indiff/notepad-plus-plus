@echo off
git config merge.ours.driver true
echo ./lexilla merge=ours > .gitattributes
echo ./scintilla merge=ours >> .gitattributes
git add .gitattributes
git commit -m "设置合并策略以保留子模块"
git merge master