cwd=$(pwd)
echo "Step 1: Made $cwd/to.py executable"
chmod +x to.py

unameOut="$(uname -s)"
case "${unameOut}" in
  Linux*)     bashFile=~/.bashrc;;
  Darwin*)    bashFile=~/.bash_profile;;
  *)          bashFile=~/.bashrc
esac

echo "Step 2: Appended 'to' command in $bashFile"
echo "
# Added by to (https://github.com/nmoya/to.git)
to() {
  out=\`$cwd/to.py \$@\`
  if [[ \$out == c* ]]
  then
    eval \$out
  else
    echo \$out
  fi
}" >> $bashFile

echo "Step 3: Re-loading $bashFile"
source $bashFile

echo "

A few exemples to get started:

To go to ~/Documents:
Run: to doc

To go to ~/Desktop:
Run: to de

To go to ~/Pictures:
Run: to pi

To go to ~/Repositories/my-cool-app/android/app/build/outputs/apk
Run: to rmyaaboa

Running: to d
Will print ['Downloads', 'Desktop', 'Documents'] so you can fix your input
"

echo "Enjoy to!"
