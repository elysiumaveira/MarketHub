import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import CustomBottomNavigation from './MobileBottomNav.styles'

import {
    BottomNavigationAction, 
    useMediaQuery, 
} from '@mui/material'
import { useTheme } from '@mui/material/styles'
import PersonIcon from '@mui/icons-material/Person'
import FavoriteIcon from '@mui/icons-material/Favorite'
import TextsmsIcon from '@mui/icons-material/Textsms'
import MenuIcon from '@mui/icons-material/Menu'
import HomeIcon from '@mui/icons-material/Home'

export default function MobileBottomNav() {
    const [value, setValue] = useState(0)
    const navigate = useNavigate()
    const theme = useTheme()
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'))

    if (!isMobile) return null 

    return (
        <CustomBottomNavigation value={value} onChange={(event, value) => {setValue(newValue)}} showLabels>
                <BottomNavigationAction
                    label='Главная'
                    icon={<HomeIcon fontSize='large' />}
                    onClick={()=>navigate('/')}
                    sx={{
                        padding:0,
                        height: 56,
                        width: 86
                    }}
                />
                <BottomNavigationAction
                    label='Избранное'
                    icon={<FavoriteIcon fontSize='large' />}
                    onClick={()=>navigate('/')}
                    sx={{
                        padding:0,
                        height: 56,
                        width: 86
                    }}
                />
                <BottomNavigationAction
                    label='Мои объяв.'
                    icon={<MenuIcon fontSize='large' />}
                    onClick={()=>navigate('/')}
                    sx={{
                        padding:0,
                        height: 56,
                        width: 86
                    }}
                />
                <BottomNavigationAction
                    label='Сообщения'
                    icon={<TextsmsIcon fontSize='large' />}
                    onClick={()=>navigate('/')}
                    sx={{
                        padding:0,
                        height: 56,
                        width: 86
                    }}
                />
                <BottomNavigationAction
                    label='Профиль'
                    icon={<PersonIcon fontSize='large' />}
                    onClick={() => navigate('/')}
                    sx={{
                        padding:0,
                        height: 56,
                        width: 86
                    }}
                />
        </CustomBottomNavigation>
    )
}