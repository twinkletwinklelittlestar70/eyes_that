export const getAllImages = (number = 5) => {
    return fetch('/api/get_images?number=' + number, { // TODO: 改一下query拼接方法，不要手动拼
        method: 'GET'
    }).then((res) => {
        return res.json()
    }).catch(e => console.error(e))
}

export const uploadAndRecognizeImage = (fileData) => {
    let imgFile = new FormData();
    imgFile.append("fileType", "IMAGE");
    imgFile.append("file", fileData);

    return fetch('/api/upload_to_recog', {
        method: 'POST',
        body: imgFile
    }).then((res) => {
        return res.json()
    }) .catch(e => console.error(e))
}