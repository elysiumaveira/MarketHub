import { useState } from 'react'
import { Outlet, useNavigate } from 'react-router-dom'

import { useTheme } from '@mui/material/styles'
import { 
    useMediaQuery,
    AppBar, 
    Toolbar, 
    Box,
} from '@mui/material'
import IconButton from '@mui/material/IconButton'
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart'
import NotificationsIcon from '@mui/icons-material/Notifications'
import AddIcon from '@mui/icons-material/Add'

import SearchBar from '../SearchBar/SearchBar'
import MobileBottomNav from '../MobileBottomNavigation/MobileBottomNav'

export default function Layout() {
    const theme = useTheme()
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'))
    const navigate = useNavigate()  
    const [searchTerm, setSearchTerm] = useState('')
    const handleSearch = (term) => {setSearchTerm(term)}

    if (!isMobile) {return (
        null
    )} 

    return (
        <>
            <Box>
                <AppBar 
                    position='static'
                    elevation={0}
                    sx={{
                        backgroundColor: 'transparent'
                    }}
                >
                    <Toolbar sx={{padding:0}}>
                        <Box>
                            <SearchBar onSearch={handleSearch} />
                        </Box>
                        
                        <Box sx={{marginLeft: 6}}>
                            <IconButton aria-label='ShoppingCart' onClick={()=>navigate('/')}>
                                <ShoppingCartIcon />
                            </IconButton>

                            <IconButton aria-label='Notifications' onClick={()=>navigate('/')}>
                                <NotificationsIcon />
                            </IconButton>

                            <IconButton aria-label='CreateAListing' onClick={()=>navigate('/')}>
                                <AddIcon />
                            </IconButton>
                        </Box>
                    </Toolbar>
                </AppBar>
            </Box>
            
            <Box>
                <Outlet />
            </Box>

            <MobileBottomNav />
        </>
    )}