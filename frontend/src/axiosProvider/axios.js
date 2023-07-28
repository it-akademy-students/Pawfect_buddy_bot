function handleClick() {
    axios.create({
      baseURL: '127.0.0.1:5000',
      headers: {
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
      },
      withCredentials: true
    })
  
    axios.get(url:'/test')
      .then(({data}) => {
        console.log('eeeeeee', e)
      });
  }