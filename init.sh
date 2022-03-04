mkdir imp
mkdir feats
mkdir input
mkdir output
mkdir input/mens
mkdir input/womens

cd input/mens
kaggle competitions download -c mens-march-mania-2022

unzip '*.zip'
rm *.zip

cd ../womens
kaggle competitions download -c womens-march-mania-2022

unzip '*.zip'
rm *.zip