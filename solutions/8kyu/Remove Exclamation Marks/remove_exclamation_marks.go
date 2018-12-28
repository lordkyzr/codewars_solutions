package kata

import "strings"

func RemoveExclamationMarks(str string) string {
	return strings.Replace(str,"!","",-1)
}