@echo off
git config merge.ours.driver true
echo ./lexilla merge=ours > .gitattributes
echo ./scintilla merge=ours >> .gitattributes
git add .gitattributes
git commit -m "���úϲ������Ա�����ģ��"
git merge master