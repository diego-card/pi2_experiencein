import React from "react";
import { Switch, Route } from "react-router-dom";
import Login from "./Pages/Login";
import Profiles from "./Pages/Profiles";
import Register from "./Pages/Register";

export default function Routes() {
  return (
    <div>
      <Switch>
        <Route exact path="/">
          <Login />
        </Route>
        <Route exact path="/register">
          <Register />
        </Route>
        <Route exact path="/profiles">
          <Profiles />
        </Route>
      </Switch>
    </div>
  );
}
