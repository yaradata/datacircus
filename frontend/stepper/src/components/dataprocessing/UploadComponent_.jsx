import React, { useState, useEffect } from "react";

import axios from "axios";

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Radio from '@mui/material/Radio';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

// 

import { styled } from '@mui/material/styles';
import TextField from '@mui/material/TextField';



const Item = styled(Paper)(({ theme }) => ({display: 'flex'}));

const urls = {
    'common_uploadFile': 'http://test.localhost:32000/common/upload_file',
    'common_readUrl': 'http://test.localhost:32000/common/read_url',
    'common_df_columns': 'http://test.localhost:32000/common/dataframe/columns',
    'common_df': 'http://test.localhost:32000/common/read_url'
}


const Upload = ({onCheckIsFile, onGetFileData, isFile, stepIsOk}) => {


    useEffect(() => {
        // {
        //     "url": "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/crop_yield.csv",
        //     "filename": "b8e4c817-f8fe-46c5-aead-7cbcd31a6ac5#crop_yield.csv",
        //     "fileData": "static/b8e4c817-f8fe-46c5-aead-7cbcd31a6ac5#crop_yield.csv"
        //   }
        
        console.log("ueffect upload...");
    }, [onCheckIsFile, onGetFileData, isFile]);

    
    const handleUploadCheckBtn = (e) => {
        onCheckIsFile(!isFile)
    }
    

    const uploadWithUrl = (e) => {
        let data_url = e.target.value.trim();

        if (data_url.length === 0 || data_url === null) { return false }

        axios.post(
            urls.common_readUrl, {data_url:data_url, sep:','},
            {headers: {'Accept': 'application/json','Content-Type': 'application/json'}}
        )
        .then( (response) => {
            console.log('---------------------------------');
            onGetFileData(response.data)
            stepIsOk(true)
        } )
        .catch((error) => {
            console.error('Error:', error);
        });

    }

    const uploadWithBrother = (e) => {
        let files = e.target.files
        if (files.length === 0 || files.length >=2) {return False}
        
        try {
            // Update the formData object 
            const formData = new FormData(); 
            formData.append("file",files[0]);

            axios.post(urls.common_uploadFile,formData)
            .then( (response) => {
                // setFileData(response.data)
                onGetFileData(response.data)
                stepIsOk(true)
            } )
            .catch((error) => {
                console.error('Error:', error);
            });   
        } catch (error) {
            throw error
        }

    }


    // get data
    const handleGetFile = (e) => {
        e.preventDefault;
        // fileData
        // console.log('here ' + `${fileData}`);
        // console.log('here1: ' + fileData);
        // let xx = "static/6780a5f9-51c8-45bc-9693-0f5f06b39639#credit_data.csv";
        // axios.post(
        //     urls.common_df_columns,
        //     {
        //         fileData: xx,
        //         sep: ','
        //     },
        //     {
        //         headers: {
        //             'Content-Type': 'application/json'
        //         }
        //     }
        // )
        // .then((response) => {
        //     console.log(response.data);
        //     // fileData(fileData)
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        // });
    }
    // const handleGetFile = (data) => {
    //     // 
    // }

    console.log("log upload...");
    // console.log(props);


    return (
        <div style={{ width: '100%' }}>
            <Radio
                checked={isFile === true}
                value="file"
                name="radio-buttons"
                onChange={e => handleUploadCheckBtn(e)}
                inputProps={{ 'aria-label': 'File' }}
            />
            <Radio
                checked={isFile === false}
                value="url"
                name="radio-buttons"
                onChange={e => handleUploadCheckBtn(e)}
                inputProps={{ 'aria-label': 'Url' }}
            />
            <Box
                sx={{
                    display: 'flex',
                    alignItems: 'flex-start',
                    p: 1,
                    m: 1,
                    bgcolor: 'background.paper',
                    borderRadius: 1,
                    border: 6,
                    borderColor: 'red',
                    justifyContent: 'center'
                }}
            >
                { isFile === true ?
                    (
                    <Item 
                        sx={{ minWidth: 150, width: 500, maxWidth: 1200, height: 50, mx: 2 }} 
                        style={{overflow: 'hidden'}}
                    >
                        <Button 
                            variant="contained" component="label"
                            fullWidth
                            onChange={ e => uploadWithBrother(e) }
                        >
                            Upload File
                            <input type="file" hidden multiple/>
                        </Button>
                    </Item>)
                    : 
                    (<Item 
                        sx={{ minWidth: 150, width: 500, maxWidth: 1200, height: 50, mx: 2 }}
                        style={{overflow: 'hidden'}}
                    >
                        <TextField 
                            id="filled-search-train"
                            label="Url train"
                            type="search"
                            variant="filled"
                            fullWidth
                            onBlur={ e => uploadWithUrl(e) }
                        />
                        <TextField 
                            id="filled-search-test"
                            label="Url test"
                            type="search"
                            variant="filled"
                            fullWidth
                            onBlur={ e => uploadWithUrl(e) }
                        />
                    </Item>)
                }
            </Box>
        </div>
    );
}

// 




export default Upload;
