import { Box, Typography } from '@mui/material'
import OutlinedCard from '../components/Card/Card'

export default function Home() {
    return (
        <>
            <Box>
                <Typography variant='h5'>Все объявления</Typography>
                <OutlinedCard />
                <OutlinedCard />
                <OutlinedCard />
                <OutlinedCard />
                <OutlinedCard />
                <OutlinedCard />
            </Box>
        </>
    )
}