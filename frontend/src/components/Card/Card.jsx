import React from 'react'

import { Box, 
        Card, 
        CardActions, 
        CardContent, 
        Button, 
        Typography } from '@mui/material'

const bull = (
    <Box
        component="span"
        sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
        *
    </Box>
)

const card = (
    <React.Fragment>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', p: 2 }}>

            <Box sx={{ flex: 1 }}>
                <CardContent>
                    <Typography gutterBottom sx={{ color: 'text.secondary', fontSize: 14 }}>
                        23.06.2025
                    </Typography>
                    <Typography variant='h5' component='div'>
                        Да что такое ваш автомобиль
                    </Typography>
                    <Typography sx={{ color: 'text.secondary', mb: 1.5 }}>100000$</Typography>
                    <Typography variant='body2'>
                        Крутая тачка в рассрочку не дам
                        <br />
                        +375 (29) 111 22 33 
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size='small'>Learn more</Button>
                </CardActions>
            </Box>

            <Box sx={{ ml: 2 }}>
                <img src="porsche911.jpg" alt="Автомобиль" style={{ width: '150px', height: 'auto', borderRadius: 8 }} />
            </Box>
        </Box>
    </React.Fragment>
)

export default function OutlinedCard() {
    return (
        <Box sx={{minWidth: 275}}>
            <Card variant='outlined'>{card}</Card>
        </Box>
    )
}