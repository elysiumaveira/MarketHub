import stringAvatar from '../../shared/utils/StringToAvatar'

import Avatar from '@mui/material/Avatar'

export default function UserAvatar() {
    return (
        <>
            <Avatar {...stringAvatar('User Test')} />
        </>
    )
}