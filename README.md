# Trivy Image Scanner from Amazone ECR

1. Create a new `branch`
2. Add images to `images.json`
```JSON
[
    "image1:tag",
    "image2:tag",
    "image3:tag",
    "image4:tag",
    "..."
]
```
3. Create and merge pull request to the `master` branch.

## Custom settings
* Amazon registry URL and region setup as environment GHA variable `REGISTRY_URL` and `AWS_REGION`
* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as GHA secrets.