set -e
echo 'removing previous files...'
rm /run/media/ethan/disk/mathswell/*.py
echo 'saving new files...'
cp *.py /run/media/ethan/disk/mathswell/
echo 'ejecting...'
eject /run/media/ethan/disk/