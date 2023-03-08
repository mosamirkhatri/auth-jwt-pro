import { Button, ButtonProps } from "@mantine/core";
// import { GithubIcon, DiscordIcon, TwitterIcon } from '@mantine/ds';
import { TwitterIcon } from "@mantine/ds";
import { GoogleIcon } from "./GoogleIcon";

export function GoogleButton(props: ButtonProps) {
  return (
    <Button
      leftIcon={<GoogleIcon />}
      variant="default"
      color="gray"
      {...props}
    />
  );
}
// Twitter button as anchor
export function TwitterButton(
  props: ButtonProps & React.ComponentPropsWithoutRef<"a">
) {
  return (
    <Button
      component="a"
      leftIcon={<TwitterIcon size="1rem" color="#00ACEE" />}
      variant="default"
      {...props}
    />
  );
}
