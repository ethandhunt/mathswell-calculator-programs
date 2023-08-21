set -e
mkdir -p /run/media/ethan/disk/mathswell
echo 'removing previous files...'
rm /run/media/ethan/disk/mathswell/*.py
echo 'saving new files...'
cp *.py /run/media/ethan/disk/mathswell/
echo 'ejecting...'
sudo eject /run/media/ethan/disk/