export interface User{
    id: number,
    username: string,
    email: string,
    is_staff: boolean,
    first_name: string,
    last_name: string
}

// user title  content img_url  date_created  date_modified 
export interface Post{
    id: number,
    user: number,
    content: string,
    img_url: string, 
    date_created: Date,
}
