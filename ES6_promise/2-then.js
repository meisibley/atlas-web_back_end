export default function handleResponseFromAPI(promise) {
  return promise.then(() => {
    return ({
      status: 200,
      body: success,
    });
  }).catch(() => {
    console.log('Got a response from the API');
    return (new Error());
  });
}
