using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for DatabasePage.xaml
    /// </summary>
    public partial class DatabasePage : Page
    {
        public DatabasePage()
        {
            InitializeComponent();
            PopulateDatabaseList();
        }

        private void PopulateDatabaseList()
        {
            lv_database.Items.Clear();
                var sCount = Properties.Settings.Default.Databases.Count;
                if (sCount > 0)
                {
                    string[] serverList = new string[sCount];
                    Properties.Settings.Default.Databases.CopyTo(serverList, 0);
                    foreach (var x in serverList)
                    {
                        lv_database.Items.Add(x);
                    }
                }

        }

        private void btnAddDB_Click(object sender, RoutedEventArgs e)
        {
            var nDatabase = DatabaseTextBox.Text;
            if (string.IsNullOrEmpty(nDatabase))
            {
                MessageBox.Show("Please enter a valid server");
                return;
            }
            var result = MessageBox.Show($"Add Database \"{nDatabase}\" to list?", "Add Database", MessageBoxButton.OKCancel);
            if (result == MessageBoxResult.OK)
            {
                AddDatabase(nDatabase);
            }

        }

        private void AddDatabase(string nDatabase)
        {
            try
            {
                // TODO Check if setting exists
                Properties.Settings.Default.Databases.Add(nDatabase);
                Properties.Settings.Default.Save();
                DatabaseTextBox.Text = "";
                PopulateDatabaseList();
            }
            catch (NullReferenceException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void btnDelete_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                if (lv_database.SelectedValue != null)
                {
                    var delDB = lv_database.SelectedValue.ToString();
                    var result = MessageBox.Show($"Remove \"{delDB}\"?", "Remove Server", MessageBoxButton.OKCancel);
                    if (result == MessageBoxResult.OK)
                    {
                        RemoveDatabase(delDB);
                    }
                }
                else
                { MessageBox.Show($"Please select an item to delete"); }
            }
            catch (Exception ex)
            {

                MessageBox.Show($"Oops, please close application and try again. Error:{ex.ToString()}");
            }

        }

        private void RemoveDatabase(string delDB)
        {
            try
            {
                // TODO Check if setting exists
                Properties.Settings.Default.Databases.Remove(delDB);
                Properties.Settings.Default.Save();
                DatabaseTextBox.Text = "";
                PopulateDatabaseList();
            }
            catch (NullReferenceException ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mw = Application.Current.Windows.OfType<MainWindow>().FirstOrDefault();
            if (mw != null)
            {
                mw._mainFrame.NavigationService.RemoveBackEntry();
                mw._mainFrame.Content = new MainPage();
            }
        }
    }
}
