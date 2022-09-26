import React, { useEffect, useState } from 'react';
import axios from "axios";

import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';


import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';
// import DoneIcon from '@mui/icons-material/Done';
// import DeleteIcon from '@mui/icons-material/Delete';


import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

import ListItem from '@mui/material/ListItem';




const urls = {
    'common_uploadFile': 'http://test.localhost:32000/common/upload_file',
    'common_readUrl': 'http://test.localhost:32000/common/read_url',
    'common_df_columns': 'http://test.localhost:32000/common/dataframe/columns',
    'common_df': 'http://test.localhost:32000/common/read_url'
}

const  Splitting = ({fileInfo, fileColumns, stepIsOk, trainLabel, trainFeatures}) => {

    const [columns, setColumns] = useState([]);
    const [label, setLabel] = useState([]);
    const [features, setFeatures] = useState([]);

    useEffect( () => {
        
        // get columns
        axios.post(
            urls.common_df_columns,
            {filepath: fileInfo.filepath,sep: ','},
            {headers: {'Accept': 'application/json','Content-Type': 'application/json'}}
        )
        .then((response) => {
            fileColumns(response.data); 
            setColumns(response.data.columns); 
            stepIsOk(true);
            
            setFeatures(response.data.columns);
            trainFeatures(response.data.columns);
        })
        .catch((error) => {
            console.error('Error:', error.code);
        });

    }, []);


    const handleDelete = (data, tab) => (e) =>{
        e.preventDefault;
        setFeatures((tab) => tab.filter((t) => t !== data)); trainFeatures((tab) => tab.filter((t) => t !== data));
        
    };

    const handleDeleteLabel = (data) => () => {
        setFeatures([...features, ...data]); trainFeatures([...features, ...data]);
        setLabel([]);  trainLabel([]);
    }

    const handleClick = (data) => () => {
        if( label.length !==0 ){
            setFeatures([...features, ...label]); trainFeatures([...features, ...label]);
        }
        setFeatures((tab) => tab.filter((t) => t !== data)); trainFeatures((tab) => tab.filter((t) => t !== data));
        setLabel([data]); trainLabel([data]);
    }


    
    return (
        <div>
            <Typography variant="h5" component="h5">Choose label column</Typography>
           
            <Grid container spacing={2}>

                <Grid item xs={8}>
                    <Typography variant="h5" component="h5">Features</Typography>
                    <Paper
                        sx={{display: 'flex', justifyContent: 'center', flexWrap: 'wrap', listStyle: 'none', p: 0.5, m: 2 }}
                        component="ul"
                        >
                        {features && features.map((data, key) => {
                            return (
                                <Chip 
                                key={key}
                                // icon={icon}
                                label={data}
                                onDelete={handleDelete(data, features)}
                                onClick={handleClick(data)}
                                />
                            );
                        })}
                    </Paper>
                </Grid>
                <Grid item xs={4}>
                    <Typography variant="h5" component="h5">Label</Typography>
                    <Paper
                    sx={{display: 'flex', justifyContent: 'center', flexWrap: 'wrap', listStyle: 'none', p: 0.5, m: 2,}}
                    component="ul"
                    >
                    {
                        label && label.length !== 0 ? (<Chip label={label} onDelete={handleDeleteLabel(label)} />) : null
                    }
                    </Paper>
                </Grid>
            </Grid>

            {/* <Stack direction="row" spacing={1}></Stack> */}


            <hr />
        </div>
    );
}

export default Splitting;

// https://drive.google.com/drive/folders/13jSCthw4ycYHdYY7TkC2uWygtEFG8EjW?usp=sharing
// https://github.com/m-ahmedy/alx-thu5-ansible-exercise
