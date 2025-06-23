import { useState, useEffect } from 'react'

import { TextField } from '@mui/material'
import { InputAdornment } from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'

export default function SearchBar({ placeholder = 'Поиск...', onSearch }) {
    const [isMobile, setIsMobile] = useState(false)

    useEffect(() => {
        const mediaQuery = window.matchMedia('(max-width: 780px)')
        const handler = (e) => setIsMobile(e.matches)
        handler(mediaQuery)
        mediaQuery.addEventListener('change', handler)
        return () => mediaQuery.removeEventListener('change', handler)
    }, [])

    return (
        <TextField 
            fullWidth
            variant='outlined'
            size='small'
            placeholder={placeholder}
            onChange={(e) => onSearch(e.target.value)}
            sx={{
                maxWidth: isMobile ? '100%' : '200%', 
                backgroundColor: '#f0f0f0', 
                borderRadius: '16px',
                '& .MuiOutlinedInput-notchedOutline': {border: 'none'},
            }}
            slotProps={{
                input: {
                    endAdornment: (
                        <InputAdornment position='end'>
                            <SearchOutlined />
                        </InputAdornment>
                    )
                }
            }}
        />
    )
}