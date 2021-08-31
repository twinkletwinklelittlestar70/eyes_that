echo "Start moving the build result to backend!"
rm -rf ../backend/static/*
mv ./dist/* ../backend/static
echo "Moving Finish!"