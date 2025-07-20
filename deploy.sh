./hugo
cp -r public/* ../machfivetech
cd ../machfivetech
git status
git add -A
git commit -m w5t_hugo_publish
git push