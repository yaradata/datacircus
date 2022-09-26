import React from 'react';

import UploadType from './UploadType'

import upLoadFileSvc from '../../services/upload.file'

const UploadData = async (props) => {
    let uri = '/common/status'

    let r = await upLoadFileSvc(uri=uri)

    console.log("response..");
    console.log(r)
    
    return (
        <div>
            <UploadType/>
        </div>
    );
}

export default UploadData;