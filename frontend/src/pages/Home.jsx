import React from 'react'

import { Box, Card, CardActions, CardContent, Button, Typography } from '@mui/material'
import OutlinedCard from '../components/Card'

export default function Home() {
    return (
        <>
            <Box>
                <p style={{fontSize: 28, width: '100%', margin: 0}}>Все объявления</p>
                <OutlinedCard></OutlinedCard>
                <OutlinedCard></OutlinedCard>
                <OutlinedCard></OutlinedCard>
                <OutlinedCard></OutlinedCard>
                <OutlinedCard></OutlinedCard>
                <OutlinedCard></OutlinedCard>
            </Box>
        </>
    )
}
