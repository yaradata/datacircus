import React, { useState, useEffect } from "react";

import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import StepContent from '@mui/material/StepContent';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

// 
import Upload from './UploadComponent_'

import ChooseFeaturesAndLabel from './ChooseFeaturesAndLabel'




const steps = [
    {
        label: 'Upload Training File',
        description: `For each ad campaign that you create, and more.`,
        component: true,
        componentName: 'uploadTraining'
    },
    {
        id: 2,
        label: 'Show Training File Info',
        description: 'Get training file columns, shape and dtype.',
        component: false
    },
    {
        label: 'Choose Feature and Label',
        description: 'An ad group contains one or more ads which target a shared set of keywords.',
        component: true,
        componentName: 'splitting'
    },
    {
        label: 'Upload Evaluate File',
        description: `For each ad campaign that you create, and more.`,
        component: false,
        componentName: 'upload'
    },
    {
        label: 'Show Evaluate Info',
        description: `For each ad campaign that you create, and more.`,
        component: false,
        componentName: 'upload2'
    }
];


const DataProcessing = (props) => {
    const [activeStep, setActiveStep] = useState(0);
    const [stepIsOk, setStepIsOk] = useState(!true);

    const [isFile, setIsFile] = useState(true);

    // get data 
    const [getFileInfo, setGetFileInfo] = useState();
    // splitting
    const [fileInfoColumns, setFileInfoColumns] = useState();
    const [trainLabel, setTrainLabel] = useState([]);
    const [trainFeatures, setTrainFeatures] = useState([]);
    // // training
    // const [trainning_, setTrainning_] = useState([]);
    // // prediction
    // const [prediction_, setPrediction_] = useState([]);
    
    useEffect(() => {
        console.log("ueffect stepper...");
    }, [getFileInfo, fileInfoColumns, trainFeatures, trainLabel]);

    const handleNext = () => {
        setActiveStep((prevActiveStep) => prevActiveStep + 1);
    };
    const handleBack = () => {
        setActiveStep((prevActiveStep) => prevActiveStep - 1);
    };
    const handleReset = () => {
        setActiveStep(0);
    };
    const handleDisableContinueBtn = () => {
        setStepIsOk(false)
    }

    // get data
    function handleUploadCheckBtn(newValue){
        setIsFile(newValue);
    }
    function handleGetFile(data){
        setGetFileInfo(data);
    }
    // splitting
    function handleFileInfoColumns(columns){
        setFileInfoColumns(columns);
    }
    function handleLabel(label){
        setTrainLabel(label);
    }
    function handleFeatures(features){
        setTrainFeatures(features);
    }
    
    

    console.log("log stepper...");
    console.log(trainFeatures);
    console.log(trainLabel);


  return (
        <Box>
            <Stepper activeStep={activeStep} orientation="vertical">
                {
                steps.map((step, index) => (
                    <Step key={step.label}>
                        <StepLabel
                            optional={
                                index === steps.length ? (
                                <Typography variant="caption">Last step</Typography>
                                ) : null
                            }
                        >
                            <Typography variant="h6">{step.label}</Typography>
                        </StepLabel>

                        <StepContent>

                            <Typography variant="h6">{step.description}</Typography>

                            { 
                                step.component && step.componentName === 'uploadTraining' ? <Upload isFile={isFile} onCheckIsFile={handleUploadCheckBtn} onGetFileData={handleGetFile}  stepIsOk={handleDisableContinueBtn}/> : null 
                            }

                            {
                                step.component && step.componentName === 'splitting' ? <ChooseFeaturesAndLabel fileInfo={getFileInfo} fileColumns={handleFileInfoColumns} stepIsOk={handleDisableContinueBtn} trainLabel={handleLabel}  trainFeatures={handleFeatures}/> : null
                            }

                        
                            <Box sx={{ mb: 2 }}>
                                <div>
                                    <Button
                                        variant="contained"
                                        onClick={handleNext}
                                        sx={{ mt: 1, mr: 1 }}
                                        disabled={stepIsOk}
                                    >
                                        {index === steps.length ? 'Run' : 'Continue'}
                                    </Button>
                                    <Button
                                        disabled={index === 0}
                                        onClick={handleBack}
                                        sx={{ mt: 1, mr: 1 }}
                                    >
                                        Back
                                    </Button>
                                </div>
                            </Box>

                        </StepContent>
                    </Step>
                ))
                }

            </Stepper>
            {
                activeStep === steps.length - 1  && (
                    <Paper square elevation={0} sx={{ p: 3 }}>
                        <Typography>All are finished</Typography>
                        <Button onClick={handleReset} sx={{ mt: 1, mr: 1 }}>
                            Reset
                        </Button>
                    </Paper>
                )
            }
        </Box>
    );
}


export default DataProcessing;
