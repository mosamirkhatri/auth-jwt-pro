import axios from "axios";
import React from "react";

const Protected = () => {
  React.useEffect(() => {
    axios
      .post("/auth/protected-admin-request", { hello: "world", world: "hello" })
      .then(({ data }) => console.log(data));
  }, []);
  return <div>Protected</div>;
};

export default Protected;
