import axios from 'axios';

const BASE_URL = `http://localhost:8070`

class SvcUploadFile {
    constructor(uri) {
        self.uri = uri 
        self.url = BASE_URL + self.uri
    }

}

const upLoadFileSvc = async (uri) => {
    let url = BASE_URL + uri 

    axios.get(url)
    .then((res) => { 
        return []
        // return res.data 
    })
    .catch((err) => {
        return err 
    }) 
}

export default upLoadFileSvc;