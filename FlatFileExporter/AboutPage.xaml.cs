using FlatFileExporter.Models;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;


namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for AboutPage.xaml
    /// </summary>
    public partial class AboutPage : Page
    {
        public AboutPage()
        {
            InitializeComponent();
        }

        public string vrsn = "0.0.1.2";

        #region Support Links to repo

        private void btnSupportDocs(object sender, RoutedEventArgs e)
        {
            Process.Start("https://bitbucket.org/eddyizm/flatfileexporter/wiki/Home");
            e.Handled = true;
        }

        private void btnIssues(object sender, RoutedEventArgs e)
        {
            Process.Start("https://bitbucket.org/eddyizm/flatfileexporter/issues?status=new&status=open");
            e.Handled = true;
        }

        private void btnCoffee(object sender, RoutedEventArgs e)
        {
            Process.Start("https://ko-fi.com/eddyizm");
            e.Handled = true;
        }

        #endregion

        private void test(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("hello");
            checkversion();
            
        }

        private void Contribute_Expanded(object sender, RoutedEventArgs e)
        {
            CurrentIssues.IsExpanded = false;
        }

        private void checkversion()
        {
            try
            {
                var client = new RestClient("http://127.0.0.1:8000/api/v1/flat_file_version");
                client.Timeout = -1;
                var request = new RestRequest(Method.GET);
                IRestResponse response = client.Execute(request);
                var result = JsonConvert.DeserializeObject<VersionCheck>(response.Content);

                var version1 = new Version(result.version);
                var version2 = new Version(vrsn);
                var versionResult = version1.CompareTo(version2);

                if (versionResult > 0)
                {
                    MessageBox.Show($"New Version Available: {result.version}\n" +
                    $"Last Updated: {String.Format("{0:d}", result.dateUpdated)}\n" +
                    $"Link: {result.URL}");
                }
                else
                {
                    MessageBox.Show($"Software Up to Date: {vrsn}\n");
                }
               

                
            }
            catch (Exception)
            {
                MessageBox.Show($"Error contacting Server. Are you offline?");
            }


        }

    }
}


    